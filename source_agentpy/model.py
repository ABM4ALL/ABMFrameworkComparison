import agentpy as ap
import numpy as np
import pandas as pd

from source_agentpy.agent import CovidAgent


class CovidModel(ap.Model):

    def setup(self):
        """ Initiate a list of new agents. """
        self.agents = ap.AgentList(self, self.p['agent_num'], cls=CovidAgent)
        self.transition_probs = self.init_transition_probs()
        self.steps = self.p['period_num']
        self.num_agents = self.p["agent_num"]
        self.initial_infected_percentage = self.p["initial_infected_percentage"]
        self.young_percentage = self.p["young_percentage"]
        self.infection_prob = self.p["infection_prob"]

        for agent in self.agents:
            agent.health_state = self.create_health_state()
            agent.age_group = self.create_age_group()

        self.s0 = 0
        self.s1 = 0
        self.s2 = 0
        self.s3 = 0

    def step(self):
        """ Call a method for every agent. """
        infection_prob = (self.s1 / self.num_agents) * self.infection_prob
        self.agents.infection(infection_prob)
        self.agents.health_state_transition()
        self.calc_population_infection_state()
        self.record(['s0', 's1', 's2', 's3'])

    def update(self):
        """ Record a dynamic variable. """

        if self.t >= self.steps:
            self.stop()

    def end(self):
        """ Repord an evaluation measure. """
        # self.report('my_measure', self.log)
        self.report("data", self.log)
        # print(self.log)

    def create_health_state(self):
        state = 0
        if np.random.uniform(0, 1) <= self.initial_infected_percentage:
            state = 1
        return state

    def create_age_group(self: "CovidScenario"):
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

    def agents_infection(self, agents: "AgentList[CovidAgent]"):
        infection_prob = (self.s1 / self.num_agents) * self.scenario.infection_prob
        for agent in agents:
            if agent.health_state == 0:
                agent.infection(infection_prob)

    def calc_population_infection_state(self):
        self.reset_counters()
        agent: 'CovidAgent'
        for agent in self.agents:
            if agent.health_state == 0:
                self.s0 += 1
            elif agent.health_state == 1:
                self.s1 += 1
            elif agent.health_state == 2:
                self.s2 += 1
            else:
                self.s3 += 1
