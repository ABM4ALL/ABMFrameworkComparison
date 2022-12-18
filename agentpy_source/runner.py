# -*- coding:utf-8 -*-
# @Time: 2022/12/18 18:18
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: runner.py
import os.path

import agentpy as ap
import pandas as pd
from matplotlib import pyplot as plt

from .config import DATA_FOLDER

from .model import CovidModel


def run():
    parameters = pd.read_excel(os.path.join(DATA_FOLDER, 'input', 'SimulatorScenarios.xlsx'))
    exp = ap.Experiment(CovidModel, parameters.to_dict('records'))
    results = exp.run()
    reporters: pd.DataFrame = results['reporters']
    for param in parameters.to_dict(orient='records'):
        data = reporters.iloc[param['id'], :]['data']
        plt.figure()
        plt.title(f"Scenario {param['id']}")
        plt.plot(data['s0'], label='not_infected')
        plt.plot(data['s1'], label="infected")
        plt.plot(data['s2'], label="recovered")
        plt.plot(data['s3'], label="dead")
        plt.xlabel("Step")
        plt.ylabel("Count")
        plt.legend()
    plt.show()
