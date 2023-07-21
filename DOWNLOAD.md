Dataset **Synthetic plants** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/P/l/sT/892nWHWBctcvD4Gub4rGxdPo0o90EkhnR36X820VehrxtC4rRHqof80eOsa5W2UCkeARLCqlcjjbgAM1d0n6kDVZ18qLeZjeSn5wLcr3cq75sbEWVHVZYDqf4Q4Y.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Synthetic plants', dst_path='~/dtools/datasets/Synthetic plants.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/harlequeen/synthetic-rgbd-images-of-plants/download?datasetVersionNumber=3)