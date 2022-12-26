## H2O Installation

1. Install dependencies

```shell
pip install requests
pip install tabulate
pip install future
```

2. Use `pip` or `conda` to install this version of the H2O Python module.

```shell
pip install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
```

```shell
conda install -c h2oai h2o
```
## Test Usage

```shell
python test.py --task [classification | regression] --id [task_id] --ip [server-ip:port] --max_runtime [seconds] --algorithms [algo1,algo2,algo3,...]
```

## Test Cases

### Classification 1

Classification task to predict future backordered products which is a common supply chain problem.
> Product Backorder Dataset
` https://www.kaggle.com/competitions/untadta/data`

### Classification 2

Classification task to predict the electric devices from behavioral data about how consumers use electricity. The dataset has different electric devices as classes.
> Electric Devices Dataset
` http://www.timeseriesclassification.com/description.php?Dataset=ElectricDevices `

### Classification 3

Classification task to predict types of the mushrooms for given mushroom attributes.
> Mushroom Dataset
` https://archive.ics.uci.edu/ml/datasets/Secondary+Mushroom+Dataset `

### Classification 4

> Insect Sound Dataset
` http://www.timeseriesclassification.com/description.php?Dataset=InsectSound `

### Classification 5

Regression task to predict the net hourly electrical energy output of a power plant from hourly average ambient variables Temperature, Ambient Pressure, Relative Humidity, and Exhaust Vacuum.
> Combined Cycle Power Plant
` http://archive.ics.uci.edu/ml/datasets/Combined+Cycle+Power+Plant`

##### Additional Datasets
> Face Detection
` http://www.timeseriesclassification.com/description.php?Dataset=FaceDetection `

> Melbourne Pedestrian
` http://www.timeseriesclassification.com/description.php?Dataset=MelbournePedestrian `