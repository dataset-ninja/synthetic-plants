**Synthetic RGB-D Data for Plant Segmentation** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. Possible applications of the dataset could be in the agricultural industry. 

The dataset consists of 10000 images with 326754 labeled objects belonging to 4 different classes including *leaf*, *petiole*, *stem*, and other: *fruit*.

Images in the Synthetic Plants dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 2 (0% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. The dataset was released in 2018.

Here is the visualized example grid with animated annotations:

[animated grid](https://github.com/dataset-ninja/synthetic-plants/raw/main/visualizations/horizontal_grid.webm)
