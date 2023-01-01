import os

import matplotlib.pyplot as plt


def plot_result(df, scenario_id):
    plt.figure()
    plt.title(f"Scenario {scenario_id}")
    plt.plot(df.s0, label='not_infected')
    plt.plot(df.s1, label="infected")
    plt.plot(df.s2, label="recovered")
    plt.plot(df.s3, label="dead")
    plt.xlabel("Step")
    plt.ylabel("Count")
    plt.legend()
    plt.savefig(
        os.path.join(
            os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/output"),
            f"Mesa_PopulationInfection_S{scenario_id}" + ".png"
        ),
        dpi=200,
        format="PNG",
    )
