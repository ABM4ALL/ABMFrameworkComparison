import mesa
import numpy as np
import pandas as pd

from source_mesa.agent import CovidAgent


class CovidModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, **kwargs):
        super().__init__()

        self.id_scenario = kwargs['id']
        self.agent_num = kwargs['agent_num']
        self.initial_infected_percentage = kwargs['initial_infected_percentage']
        self.young_percentage = kwargs["young_percentage"]
        self.infection_prob = kwargs["infection_prob"]

        # Counter for different health states
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0
        self.schedule = mesa.time.SimultaneousActivation(self)

        # Create agents
        for i in range(self.agent_num):
            a = CovidAgent(i, self)
            # Initialize health state and age group
            a.health_state = self.create_health_state()
            a.age_group = self.create_age_group()
            self.schedule.add(a)

        self.datacollector = mesa.DataCollector(
            model_reporters={"s0": "s0", "s1": "s1", "s2": "s2", "s3": "s3"},
            agent_reporters={"health_state": "health_state"}
        )

        self.transition_probs = self.init_transition_probs()

    def create_health_state(self):
        state = 0
        if np.random.uniform(0, 1) <= self.initial_infected_percentage:
            state = 1
        return state

    def create_age_group(self):
        age_group = 0
        if np.random.uniform(0, 1) > self.young_percentage:
            age_group = 1
        return age_group

    def init_transition_probs(self):
        df = pd.read_excel("./data/input/Parameter_AgeGroup_TransitionProb.xlsx")
        return {
            0: {
                "s1_s1": df.at[0, "prob_s1_s1"],
                "s1_s2": df.at[0, "prob_s1_s2"],
                "s1_s3": df.at[0, "prob_s1_s3"],
            },
            1: {
                "s1_s1": df.at[1, "prob_s1_s1"],
                "s1_s2": df.at[1, "prob_s1_s2"],
                "s1_s3": df.at[1, "prob_s1_s3"],
            }
        }

    def reset_counters(self):
        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0

    def calc_population_infection_state(self):
        self.reset_counters()
        agent: 'CovidAgent'
        for agent in self.schedule.agents:
            if agent.health_state == 0:
                self.s0 += 1
            elif agent.health_state == 1:
                self.s1 += 1
            elif agent.health_state == 2:
                self.s2 += 1
            else:
                self.s3 += 1

    def step(self) -> None:
        self.schedule.step()
        self.calc_population_infection_state()
        self.datacollector.collect(self)
