import pandas as pd
import json
from time import time
from datetime import datetime
import h2o
from h2o.automl import H2OAutoML
from scipy.io.arff import loadarff


ALGORITHMS = [
    "DRF",
    "GLM",
    "XGBoost",
    "GBM",
    "DeepLearning",
    "StackedEnsemble"
    ]

class test:

    def __init__(self, h2o):
        self.h2o = h2o
        self.project_created_time = datetime.now().strftime("%Y-%m-%dT%H.%M.%S")
        self.logs = []

    def logs_save(self):
        with open('H2O/test/logs/log_' + str(self.project_created_time) + '.json', 'w') as f:
            json.dump(self.logs, f)

    def classification1(self, max_runtime_secs = 0, max_models = None, include_algos = None):
        # Dataset Location
        data_path = "https://github.com/h2oai/h2o-tutorials/raw/master/h2o-world-2017/automl/data/product_backorders.csv"
        
        # Import Data
        df = self.h2o.import_file(data_path)

        # Basic Preprocessing
        y = "went_on_backorder"
        x = df.columns
        x.remove(y)
        x.remove("sku")

        # AutoML engine
        start_time = datetime.now()
        s = time()
        aml = H2OAutoML(
            max_runtime_secs = max_runtime_secs,
            max_models = max_models,
            include_algos = include_algos,
            project_name = "classification_test_" + datetime.now().strftime("%Y-%m-%dT%H.%M.%S"))
        aml.train(x = x, y = y, training_frame = df)
        end_time = datetime.now()

        # Get learderboard
        lb = aml.leaderboard.as_data_frame().to_dict()

        # Logging
        log = {
            "experiment" : "classification_1",
            "max_runtime_secs" : max_runtime_secs,
            "max_models" : max_models,
            "include_algos" : include_algos,
            "start_time" : str(start_time),
            "end_time" : str(end_time),
            "elapsed_time" : str(end_time - start_time),
            "leaderboard" : lb,
            "event_log" : aml.event_log.as_data_frame().to_dict()
        }
        self.logs.append(log)
        self.logs_save()
        h2o.remove(aml)

    def classification2(self, max_runtime_secs = 0, max_models = None, include_algos = None):
        # Read data
        raw_data = loadarff('H2O/test/data/ElectricDevices_TRAIN.arff')
        df_data = pd.DataFrame(raw_data[0])

        # Import Data
        hf = h2o.H2OFrame(df_data)

        # Basic Preprocessing
        y = "target"
        x = hf.columns
        x.remove(y)

        # AutoML engine
        start_time = datetime.now()
        s = time()
        aml = H2OAutoML(
            max_runtime_secs = max_runtime_secs,
            max_models = max_models,
            include_algos = include_algos,
            project_name = "classification_test_" + datetime.now().strftime("%Y-%m-%dT%H.%M.%S"))
        aml.train(x = x, y = y, training_frame = hf)
        end_time = datetime.now()

        # Get learderboard
        lb = aml.leaderboard.as_data_frame().to_dict()

        # Logging
        log = {
            "experiment" : "classification_2",
            "max_runtime_secs" : max_runtime_secs,
            "max_models" : max_models,
            "include_algos" : include_algos,
            "start_time" : str(start_time),
            "end_time" : str(end_time),
            "elapsed_time" : str(end_time - start_time),
            "leaderboard" : lb,
            "event_log" : aml.event_log.as_data_frame().to_dict()
        }
        self.logs.append(log)
        self.logs_save()
        h2o.remove(aml)

    def classification3(self, max_runtime_secs = 0, max_models = None, include_algos = None):
        # Read data
        df_data = pd.read_csv("H2O/test/data/secondary_data.csv", delimiter = ";")

        # Import Data
        hf = h2o.H2OFrame(df_data)

        # Basic Preprocessing
        y = "class"
        x = hf.columns
        x.remove(y)

        # AutoML engine
        start_time = datetime.now()
        s = time()
        aml = H2OAutoML(
            max_runtime_secs = max_runtime_secs,
            max_models = max_models,
            include_algos = include_algos,
            project_name = "classification_test_" + datetime.now().strftime("%Y-%m-%dT%H.%M.%S"))
        aml.train(x = x, y = y, training_frame = hf)
        end_time = datetime.now()

        # Get learderboard
        lb = aml.leaderboard.as_data_frame().to_dict()

        # Logging
        log = {
            "experiment" : "classification_3",
            "max_runtime_secs" : max_runtime_secs,
            "max_models" : max_models,
            "include_algos" : include_algos,
            "start_time" : str(start_time),
            "end_time" : str(end_time),
            "elapsed_time" : str(end_time - start_time),
            "leaderboard" : lb,
            "event_log" : aml.event_log.as_data_frame().to_dict()
        }
        self.logs.append(log)
        self.logs_save()
        h2o.remove(aml)

    def classification4(self, max_runtime_secs = 0, max_models = None, include_algos = None):
        # Read data
        raw_data = loadarff('H2O/test/data/InsectSound_TRAIN.arff')
        df_data = pd.DataFrame(raw_data[0])

        # Import Data
        hf = h2o.H2OFrame(df_data)

        # Basic Preprocessing
        y = "target"
        x = hf.columns
        x.remove(y)

        # AutoML engine
        start_time = datetime.now()
        s = time()
        aml = H2OAutoML(
            max_runtime_secs = max_runtime_secs,
            max_models = max_models,
            include_algos = include_algos,
            project_name = "classification_test_" + datetime.now().strftime("%Y-%m-%dT%H.%M.%S"))
        aml.train(x = x, y = y, training_frame = hf)
        end_time = datetime.now()

        # Get learderboard
        lb = aml.leaderboard.as_data_frame().to_dict()

        # Logging
        log = {
            "experiment" : "classification_4",
            "max_runtime_secs" : max_runtime_secs,
            "max_models" : max_models,
            "include_algos" : include_algos,
            "start_time" : str(start_time),
            "end_time" : str(end_time),
            "elapsed_time" : str(end_time - start_time),
            "leaderboard" : lb,
            "event_log" : aml.event_log.as_data_frame().to_dict()
        }
        self.logs.append(log)
        self.logs_save()
        h2o.remove(aml)


    def regression1(self, max_runtime_secs = 0, max_models = None, include_algos = None):
        # Dataset Location
        data_path = "https://github.com/h2oai/h2o-tutorials/raw/master/h2o-world-2017/automl/data/powerplant_output.csv"

        # Import Data
        df = h2o.import_file(data_path)

        # Basic Preprocessing
        y = "HourlyEnergyOutputMW"
        splits = df.split_frame(ratios = [0.8], seed = 1)
        train = splits[0]
        test = splits[1]
    
        # AutoML engine
        start_time = datetime.now()
        aml = H2OAutoML(
            max_runtime_secs = max_runtime_secs,
            max_models = max_models,
            include_algos = include_algos,
            project_name = "regression_test_" + datetime.now().strftime("%Y-%m-%dT%H.%M.%S"))
        aml.train(y = y, training_frame = train, leaderboard_frame = test)
        end_time = datetime.now()

        # Get learderboard
        lb = aml.leaderboard.as_data_frame().to_dict()

        # Logging
        log = {
            "experiment" : "regression_1",
            "max_runtime_secs" : max_runtime_secs,
            "max_models" : max_models,
            "include_algos" : include_algos,
            "start_time" : str(start_time),
            "end_time" : str(end_time),
            "elapsed_time" : str(end_time - start_time),
            "leaderboard" : lb,
            "event_log" : aml.event_log.as_data_frame().to_dict()
        }
        self.logs.append(log)
        self.logs_save()
        h2o.remove(aml)


