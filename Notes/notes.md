# Papers notes

# Sources of dynamism
- Dynamic requests
- Trafic conditions

## A review of dynamic vehicle routing problems
https://www.sciencedirect.com/science/article/pii/S0377221712006388#b0690
### Dynamic vehicle routing problems
- Dial-a-Ride problem
- Differences with static routing
### Dynamic and deterministic routing problems
- Absence of stochastic information
- Critical information is revealed over time -> complete instance is only known at the end of the planning horizon
- Goal is to compute best solution for current state
  - Does not guarantee best solution for complete instance
- Two different approaches
    1. Periodic reoptimization
    2. Continuous reoptimization
#### Periodic reoptimization
- An optimization procedure periodically solves a static problem corresponding to the current state, either whenever the available data changes, or at fixed intervals of time – referred to as decision epochs
- It can be based on algorithms developed for static routing
- Drawback is that all the optimization needs to be performed before updating the routing plan
- Chen and Xu [29] designed a dynamic column generation algorithm (DYCOL) for the D-VRPTW
  - https://en.wikipedia.org/wiki/Column_generation
- Montemanni et al. [102] developed an Ant Colony System (ACS) to solve the D-VRP
  - An interesting feature of their approach is the use of the pheromone trace to transfer characteristics of a good solution to the next time slice.
#### Continuous reoptimization
- Maintain information on good solutions in an adaptive memory
  - https://www.sciencedirect.com/science/article/pii/S037722170000268X
- Whenever the available data changes, a decision procedure aggregates the information from the memory to update the current routing
- he advantage is that the computational capacity is maximized, possibly at the expense of a more complex implementation
- https://en.wikipedia.org/wiki/Tabu_search
### Perfrmance evaluation
- ...
  
# A self-adaptive evolutionary algorithm for dynamic vehicle routing problems with traffic congestion
https://www.sciencedirect.com/science/article/pii/S2210650218303407
## Abstract
- Because of this dynamic nature of DVRP, evolutionary algorithms (EAs) appear highly appropriate for DVRP as they search in a parallel manner with a population of solutions.
- However, the performance of EA is highly dependent on the utilised configuration. To address this issue, we propose a self-adaptive EA for DVRP
## Introduction
- Typical meta-heuristic algorithms include tabu search [11], simulated annealing [30], evolutionary algorithms [1], ant colony [10] and variable neighbourhood algorithms [15].
- Self-adaptive EA
  - Configuration (operators) are encoded in individual too
- For example the mutation operator should be applied before crossover operator. But in another case the order should be reversed. So the convergence and diversity, which are the two critical factors in any evolutionary search process, can be better maintained.
- The study uses the DVRP benchmark released by Mavrovouniotis and Yang [22].