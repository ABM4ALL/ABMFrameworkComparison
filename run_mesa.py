import os

import pandas as pd

from source_mesa.analyzer import plot_result
from source_mesa.model import CovidModel


def run_mesa():
    scenarios_df = pd.read_excel(os.path.join('data/input', 'SimulatorScenarios.xlsx'))
    for scenario_params in scenarios_df.to_dict(orient='records'):
        scenario_id = scenario_params.pop('id')
        scenario_params.pop('run_num')
        print("=" * 20, f"Running scenario {scenario_id}", "=" * 20)
        period_num = scenario_params.pop('period_num')
        model = CovidModel(**scenario_params)
        for i in range(period_num):
            model.step()
        plot_result(model, scenario_id)


if __name__ == "__main__":
    run_mesa()
