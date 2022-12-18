# -*- coding:utf-8 -*-
# @Time: 2022/12/18 17:34
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: agent.py.py
import random

import agentpy as ap


class CovidAgent(ap.Agent):

    def setup(self):
        # Initialize an attribute with a parameter

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
