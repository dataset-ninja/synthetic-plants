Dataset **Synthetic Plants** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/M/J/Ng/hF1jxzI4vb1Fz9YwcDuVfHU27jcPm02uj0THmdkTFukcJTBwEAqRhCbBvyKwEWbcjjWN0VUZgEKEezWZrvXi5tVdPZaC0RGkBtr5Sren7sKR0xfgFuIZuG9QLLgb.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Synthetic Plants', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/harlequeen/synthetic-rgbd-images-of-plants/download?datasetVersionNumber=3)