import random
from typing import TYPE_CHECKING

import mesa

if TYPE_CHECKING:
    from source_mesa.model import CovidModel


class CovidAgent(mesa.Agent):
    """An agent with fixed initial wealth."""
    model: 'CovidModel'

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.health_state: int = 0
        self.age_group: int = 0

    def infection(self, infection_prob: float):
        if self.health_state == 0:
            if random.uniform(0, 1) <= infection_prob:
                self.health_state = 1

    def health_state_transition(self):
        if self.health_state == 1:
            transition_probs: dict = self.model.transition_probs[self.age_group]
            rand = random.uniform(0, 1)
            if rand <= transition_probs["s1_s1"]:
                pass
            elif transition_probs["s1_s1"] < rand <= transition_probs["s1_s1"] + transition_probs["s1_s2"]:
                self.health_state = 2
            else:
                self.health_state = 3

    def step(self) -> None:
        infection_prob = (self.model.s1 / self.model.num_agents) * self.model.infection_prob
        self.infection(infection_prob)

    def advance(self) -> None:
        self.health_state_transition()
