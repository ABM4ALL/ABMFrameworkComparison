import os.path

import agentpy as ap
import pandas as pd

from source_agentpy.analyzer import plot_result
from source_agentpy.model import CovidModel


def run_agentpy():
    parameters = pd.read_excel(os.path.join('data/input', 'SimulatorScenarios.xlsx'))
    exp = ap.Experiment(CovidModel, parameters.to_dict('records'))
    results = exp.run()
    plot_result(results['reporters'], parameters)


if __name__ == "__main__":
    run_agentpy()
