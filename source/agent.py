import random
from typing import TYPE_CHECKING

from Melodie import Agent

if TYPE_CHECKING:
    from source.scenario import CovidScenario


class CovidAgent(Agent):
    scenario: "CovidScenario"

    def setup(self):
        self.health_state: int = 0
        self.age_group: int = 0

    def infection(self, infection_prob: float):
        if random.uniform(0, 1) <= infection_prob:
            self.health_state = 1

    def health_state_transition(self):
        if self.health_state == 1:
            transition_probs: dict = self.scenario.get_transition_probs(self.age_group)
            rand = random.uniform(0, 1)
            if rand <= transition_probs["s1_s1"]:
                pass
            elif transition_probs["s1_s1"] < rand <= transition_probs["s1_s1"] + transition_probs["s1_s2"]:
                self.health_state = 2
            else:
                self.health_state = 3
