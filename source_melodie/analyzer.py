import os

import matplotlib.pyplot as plt

from Melodie import Config
from Melodie import db


class CovidAnalyzer:
    def __init__(self, config: "Config"):
        self.fig_folder = config.output_folder
        self.db = db.create_db_conn(config)

    def save_fig(self, fig, fig_name):
        fig.savefig(
            os.path.join(self.fig_folder, fig_name + ".png"),
            dpi=200,
            format="PNG",
        )
        plt.close(fig)

    def plot_health_state_share(self, id_scenario: int = 0, id_run: int = 0):
        df = self.db.read_dataframe("environment_result")
        df = df.loc[(df["id_scenario"] == id_scenario) & (df["id_run"] == id_run)]
        values_dict = {
            "not-infected": df["s0"],
            "infected": df["s1"],
            "recovered": df["s2"],
            "dead": df["s3"],
        }
        figure = plt.figure(figsize=(6.4, 4.8))
        ax = figure.add_axes((0.12, 0.12, 0.75, 0.75))
        ax.set_ylim(0, 1000)
        ax.set_title(f"Scenario {id_scenario}")
        ax.set_xlabel("Period")
        ax.set_ylabel("Count")
        x = [i for i in range(0, len(list(values_dict.values())[0]))]
        for key, values in values_dict.items():
            ax.plot(x, values, label=key)
        ax.legend()
        self.save_fig(figure, f"Melodie_PopulationInfection_S{id_scenario}R{id_run}")
