import os

import matplotlib.pyplot as plt
import pandas as pd


def plot_result(reporters: pd.DataFrame, parameters):
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
        plt.savefig(
            os.path.join(
                os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/output"),
                f"AgentPy_PopulationInfection_S{param['id']}" + ".png"
            ),
            dpi=200,
            format="PNG",
        )
