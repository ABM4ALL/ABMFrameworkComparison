# README

To compare the three Python packages - Mesa, AgentPy, and Melodie - 
we develop the same agent-based covid contagion model with all of them. 

In the model, we make following assumptions regarding the infection in the population:

* Each agent has two attributes: `health_state` and `age_group`.
* We consider four **health states** numbered from 0 to 3, meaning "not infected", "infected", "recovered", and "dead", respectively.
* We consider two **age groups** numbered from 0 to 1, meaning "young" and "old", respectively. A young person has a higher probability to recover from infection, and an old person has a lower probability to recover from infection.
* A "not infected" person can be infected by a "infected" person. The probability is an exogenous parameter ``infection_prob``. When 10% of the people are infected, we assume a "not infected" person has 0.1 probability to contact with a "infected" person, so the total infection probability is 0.1 $\times$ ``infection_prob``.

In this [document](https://abm4all.github.io/Melodie/html/framework_comparison.html), we compared the three packages based on the example. 

