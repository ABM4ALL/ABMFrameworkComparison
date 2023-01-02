import os

import pandas as pd
from mesa.batchrunner import FixedBatchRunner

from source_mesa.analyzer import plot_result
from source_mesa.model import CovidModel


def run_mesa_with_batch_runner():
    scenarios_df = pd.read_excel(os.path.join('data/input', 'SimulatorScenarios.xlsx'))
    params = scenarios_df.to_dict(orient="records")
    runner = FixedBatchRunner(CovidModel, params, max_steps=params[0]['period_num'])
    runner.run_all()
    for i, report_value in enumerate(runner.datacollector_model_reporters.values()):
        scenario_id = params[i]['id']
        plot_result(report_value, scenario_id)


def run_mesa():
    scenarios_df = pd.read_excel(os.path.join('data/input', 'SimulatorScenarios.xlsx'))
    for scenario_params in scenarios_df.to_dict(orient='records'):
        scenario_id = scenario_params['id']
        period_num = scenario_params['period_num']
        model = CovidModel(**scenario_params)
        for i in range(period_num):
            model.step()
        plot_result(model.datacollector.get_model_vars_dataframe(), scenario_id)
        print("=" * 20, f"Scenario {scenario_id} finished", "=" * 20)


if __name__ == "__main__":
    run_mesa()
