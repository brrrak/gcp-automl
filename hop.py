import argparse
from stress_tests.H2O_tester import *

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

task = args.task
id = args.id
addr = args.addr
runtime = args.max_runtime
algos = args.algos

if algos:
    algos = algos.replace(" ","").split(",")
    for algo in algos:
        if not algo in ALGORITHMS:
            raise ValueError("Algorithm '" + algo + "' does not exist in supported ML models.")


h2o.connect(
    url = "http://" + addr
)

experiments = test(h2o)
test = {
    "classification" : {
        "1" : test.classification1,
        "2" : test.classification2,
        "3" : test.classification3
    },
    "regression" : {
        "1" : test.regression1
    }
}