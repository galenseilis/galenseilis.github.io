---
title: Implementing a M/M/1 Queue in Ciw
date: 2023-12-20 13:51:15
categories: [simulation,discrete-event-simulation,queueing-networks,ciw]
tags: [mm1-queue, simulation,discrete-event-simulation,queueing-networks,ciw,python,queue,queueing-theory,exponential-distribution,statistics,operations-research,random-variable,inter-arrival-time,service-time,random-number-generator,seed,servers]
math: true
mermaid: true
---

[Ciw](https://ciw.readthedocs.io/en/latest/) is a [Python](https://www.python.org/) package for [simulating](https://en.wikipedia.org/wiki/Discrete-event_simulation) [queueing networks](https://en.wikipedia.org/wiki/Queueing_theory). A [M/M/1 queue](https://en.wikipedia.org/wiki/M/M/1_queue) can be implemented and simulated using Ciw in the following way.

```python
import ciw

ciw.seed(2018)

ARRIVAL_TIME = 1
SERVICE_TIME = 1 / 2
HORIZON = 365

network = ciw.create_network(
    arrival_distributions = [ciw.dists.Exponential(ARRIVAL_TIME)],
    service_distributions = [ciw.dists.Exponential(SERVICE_TIME)],
    number_of_servers = [1]
    )
    
simulation = ciw.Simulation(network)
simulation.simulate_until_max_time(HORIZON)
records = simulation.get_all_records()
```
