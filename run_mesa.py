import os

import pandas as pd
from mesa.batchrunner import FixedBatchRunner

from source_mesa.analyzer import plot_result
from source_mesa.model import CovidModel


def run_mesa():
    scenarios_df = pd.read_excel(os.path.join('data/input', 'SimulatorScenarios.xlsx'))
    params = scenarios_df.to_dict(orient="records")
    runner = FixedBatchRunner(CovidModel, params, max_steps=params[0]['period_num'])
    runner.run_all()
    for i, report_value in enumerate(runner.datacollector_model_reporters.values()):
        scenario_id = params[i]['id']
        plot_result(report_value, scenario_id)


if __name__ == "__main__":
    run_mesa()
