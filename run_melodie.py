import os

from Melodie import Config
from Melodie import Simulator

from source_melodie.analyzer import CovidAnalyzer
from source_melodie.data_loader import CovidDataLoader
from source_melodie.model import CovidModel
from source_melodie.scenario import CovidScenario

config = Config(
    project_name="Melodie_CovidContagion",
    project_root=os.path.dirname(__file__),
    input_folder="data/input",
    output_folder="data/output",
)

simulator = Simulator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        data_loader_cls=CovidDataLoader
    )

analyzer = CovidAnalyzer(config)


if __name__ == "__main__":
    simulator.run()
    analyzer.plot_health_state_share(id_scenario=0)
    analyzer.plot_health_state_share(id_scenario=1)
