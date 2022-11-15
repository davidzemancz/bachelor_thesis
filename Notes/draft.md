# Approximate solutions for (dynamic) constrained VRP

## Goals
* Find ways to process request from customers in realtime in dynamic VRP
* Descripe solution approaches using different techniques like LP, GA, AC
* Mesaure performance of those techniques and compare them

## Introduction
### Motivation
* Last-mile delivery (food, goods)
* Taxi serivces
### Related problems
* TSP - VRP si generalization
* https://en.wikipedia.org/wiki/Travelling_salesman_problem
### Hardness - NP-completeness
* VRP is extnesion of TSP and TSP is NP-complete

### Related work
#### MFF
* https://dspace.cuni.cz/handle/20.500.11956/148271
* https://dspace.cuni.cz/handle/20.500.11956/127942
* https://dspace.cuni.cz/handle/20.500.11956/82513
#### Dynamic VRP
* https://www.sciencedirect.com/science/article/abs/pii/S2210650218303407
* https://www.sciencedirect.com/science/article/pii/S0377221712006388
* https://www.mdpi.com/2073-8994/11/4/546/htm
* https://www.researchgate.net/publication/260401175_The_Dynamic_Vehicle_Routing_Problem
* https://www.sciencedirect.com/science/article/pii/S0045790617304494

## Dynamic VRP
### Mathematical model
* Dynamic
  * Request from customers appear dynamiclly
  * What 'optimal' solution is?
* In undirected graph in euclidean space
* Time windows
* Vehicles capacities
* Multi pickup
* Working hours
* Electric vehicles
* Resources

### Problem definition
* We are woking in discrete time, current time is stated by variable (or index) t
* We start at time t=0 with fixed fleet of vehicles of certain capacity, each vehicle has
    * Capacity
    * Price per km
    * Price per hour
* There are no fixed locations, new request can appear anywhere on map (map is euclidean space with metric d) - location of pickup
* Request includes several informations that dont chagne anymore (in future, request canceling could be assumed)
  * Pick-up location
  * Pick-up time window (maximal waiting time)
  * Drop-off location
  * Drop-off time wondow (endmost time of arrival)
  * Amount of goods (persons, parcels...)
  * Maximal price ??? (in practise, price may be customer accepted or denied by customer)
* Every time new request apperas recalculation of current plan is needed
  * Simple approach
    * Each vehicles has its queue of cutomers
    * Try new customer add to queue of every vehicle and select the best one
  * Complicated approach (but more accurate)
    * Solve VRP
    * We need to take into account that some vehicles are driving so theirs locations is changing permanently
      * This can be solved by solving VRP assuming vehicles location in next pick-up


### Possible approaches

#### Naive


#### Linear programming


#### GA


## Approximate solution approaches
* https://openreview.net/pdf?id=BJe1334YDH
### Linear programming
### Genetics algorithms
* https://www.sciencedirect.com/science/article/pii/S1877750317303848
* https://www.researchgate.net/publication/265888654_Solving_the_Vehicle_Routing_Problem_using_Genetic_Algorithm
### PSO techniques
* https://www.sciencedirect.com/science/article/pii/S0305054808000774
### Ant colony
* Decision making
* https://www.sciencedirect.com/science/article/pii/S1474034604000060
* https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms
* http://ktiml.mff.cuni.cz/~pilat/cs/prirodou-inspirovane-algoritmy/hejna-kolonie/
### Simulated annealing

## Experiments and analyses
* Implementations in python
* Comparsion with known solutions (google or tools)
