# https://www.kaggle.com/datasets/harlequeen/synthetic-rgbd-images-of-plants

import glob
import os

import cv2
import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from supervisely.io.fs import get_file_name, get_file_name_with_ext

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "True"


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/iwatkot/Downloads/ninja-datasets/synthetic-plants/"
    ds_name = "ds"
    batch_size = 30

    def exr_to_np(image_path):
        im = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        im = im * 255
        im[im > 255] = 255
        im = np.uint16(im)
        return im

    def create_ann(image_path):
        labels = []

        ann_path = os.path.join(annotations_folder, get_file_name_with_ext(image_path))
        ann_np = cv2.imread(ann_path, cv2.IMREAD_UNCHANGED)[:, :, 0]
        indexes = np.unique(np.uint8(ann_np))
        for idx in indexes:
            if idx != 0:
                obj_class = idx_to_obj_class[idx]
                mask = ann_np == idx
                ret, curr_mask = connectedComponents(mask.astype("uint8"), connectivity=8)
                for i in range(1, ret):
                    obj_mask = curr_mask == i
                    curr_bitmap = sly.Bitmap(obj_mask)
                    if curr_bitmap.area > 50:
                        curr_label = sly.Label(curr_bitmap, obj_class)
                        labels.append(curr_label)

        return sly.Annotation(img_size=(224, 224), labels=labels)

    obj_class_leaf = sly.ObjClass("leaf", sly.Bitmap)
    obj_class_petiole = sly.ObjClass("petiole", sly.Bitmap)
    obj_class_stem = sly.ObjClass("stem", sly.Bitmap)
    obj_class_fruit = sly.ObjClass("fruit", sly.Bitmap)
    obj_class_collection = sly.ObjClassCollection(
        [obj_class_leaf, obj_class_petiole, obj_class_stem, obj_class_fruit]
    )

    idx_to_obj_class = {
        1: obj_class_stem,
        2: obj_class_leaf,
        3: obj_class_petiole,
        4: obj_class_fruit,
    }

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project.id, meta.to_json())
    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    images_folder = os.path.join(dataset_path, "rgb_map")
    annotations_folder = os.path.join(dataset_path, "semantic_map/segmentation2_map")
    images_pathes = glob.glob(images_folder + "/*/*/*.exr")

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_pathes))

    for images_path_batch in sly.batched(images_pathes, batch_size=batch_size):
        # images_names_batch_exr = [
        #    get_file_name_with_ext(image_path) for image_path in images_path_batch
        # ]
        images_names_batch_png = [
            get_file_name(image_path) + ".png" for image_path in images_path_batch
        ]

        images_np_batch = [exr_to_np(image_path) for image_path in images_path_batch]

        img_infos = api.image.upload_nps(dataset.id, images_names_batch_png, images_np_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [create_ann(image_path) for image_path in images_path_batch]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.iters_done_report(len(images_path_batch))

    return project
