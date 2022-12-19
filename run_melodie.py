from Melodie import Simulator
from config import config
from melodie_source.data_loader import CovidDataLoader
from melodie_source.model import CovidModel
from melodie_source.scenario import CovidScenario

if __name__ == "__main__":
    simulator = Simulator(
        config=config,
        model_cls=CovidModel,
        scenario_cls=CovidScenario,
        data_loader_cls=CovidDataLoader
    )
    simulator.run()
