import argparse
from H2O_tester import *

parser = argparse.ArgumentParser(
                    prog = 'H2O Cluster Tester',
                    description = 'Sends the example test cases to H2O server.',
                    epilog = 'Help')

parser.add_argument('--task', required=True)
parser.add_argument('--id', required=True)
parser.add_argument('--addr', required=True)
parser.add_argument('--max_runtime')
parser.add_argument('--algos')

args = parser.parse_args()

task = args.task.lower()
id = args.id
addr = args.addr
runtime = args.max_runtime
algos = args.algos

if algos:
    algos = algos.replace(" ","").split(",")
    for algo in algos:
        if not algo in ALGORITHMS:
            raise ValueError("Algorithm '" + algo + "' does not exist in supported ML models.")

try:
    runtime = int(runtime)
except:
    raise ValueError("Please give max_runtime as an integer.")

h2o.connect(
    url = "http://" + addr
)

experiments = test(h2o)
tasks = {
    "classification" : {
        "1" : experiments.classification1,
        "2" : experiments.classification2,
        "3" : experiments.classification3
    },
    "regression" : {
        "1" : experiments.regression1
    }
}

tasks[task][id](max_runtime_secs=runtime, include_algos=algos)
print("# Saving")
experiments.logs_save()