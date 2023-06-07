# https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge?datasetId=27201&sortBy=voteCount

import glob
import os

import numpy as np
import supervisely as sly
from cv2 import connectedComponents
from supervisely.io.fs import get_file_name, get_file_name_with_ext


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    dataset_path = "/Users/iwatkot/Downloads/ninja-datasets/PATH/"

    return project
