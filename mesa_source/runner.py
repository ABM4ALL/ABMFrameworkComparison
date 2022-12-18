# -*- coding:utf-8 -*-
# @Time: 2022/12/18 13:30
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: runner.py
import os

import pandas as pd

from .config import DATA_FOLDER

from .model import CovidModel
import matplotlib.pyplot as plt

scenarios_df = pd.read_excel(os.path.join(DATA_FOLDER, 'input', 'SimulatorScenarios.xlsx'))


def plot_result(empty_model, scenario_id):
    df = empty_model.datacollector.get_model_vars_dataframe()

    plt.figure()
    plt.title(f"Scenario {scenario_id}")
    plt.plot(df.s0, label='not_infected')
    plt.plot(df.s1, label="infected")
    plt.plot(df.s2, label="recovered")
    plt.plot(df.s3, label="dead")
    plt.xlabel("Step")
    plt.ylabel("Count")
    plt.legend()


def run_model(**kwargs):
    scenario_id = kwargs.pop('id')
    kwargs.pop('run_num')
    period_num = kwargs.pop('period_num')
    # kwargs: {'agent_num': 1000, 'initial_infected_percentage': 0.1, 'young_percentage': 0.8, 'infection_prob': 0.1}
    print("=" * 20, f"Running scenario {scenario_id}", "=" * 20)
    empty_model = CovidModel(**kwargs)
    for i in range(period_num):
        empty_model.step()
    plot_result(empty_model, scenario_id)


def run():
    for scenario_params in scenarios_df.to_dict(orient='records'):
        run_model(**scenario_params)
    plt.show()
