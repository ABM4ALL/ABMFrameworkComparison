from Melodie import Simulator
from config import config
from source_melodie.data_loader import CovidDataLoader
from source_melodie.model import CovidModel
from source_melodie.scenario import CovidScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        data_loader_cls=CovidDataLoader
    )
    simulator.run()
