# https://developers.google.com/optimization/mip/mip_example

from ortools.linear_solver import pywraplp
from vrp import VRP, Ride
import utils

def solve(vrp : VRP):

    vehicles_count = len(vrp.vehicles)

    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    edge_vars = {}
    for u in range(vrp.nodes_count):
        for v in range(vrp.nodes_count):
            if u == v: continue

            var_key = (u, v)
            var = solver.BoolVar(str(var_key))
            edge_vars[var_key] = var

    # Constraints (https://en.wikipedia.org/wiki/Vehicle_routing_problem#Vehicle_flow_formulations)
    # 1)
    for order1 in vrp.orders:
        solver.Add(sum([edge_vars[var_key] for var_key in edge_vars if var_key[1] == order1.node]) == 1)

    # 2)
    for order1 in vrp.orders:
        solver.Add(sum([edge_vars[var_key] for var_key in edge_vars if var_key[0] == order1.node]) == 1)

    # 3)
    solver.Add(sum([edge_vars[var_key] for var_key in edge_vars if var_key[0] != vrp.depot_node and var_key[1] == vrp.depot_node]) == vehicles_count)

    # 4)
    solver.Add(sum([edge_vars[var_key] for var_key in edge_vars if var_key[0] == vrp.depot_node and var_key[1] != vrp.depot_node]) == vehicles_count)

    # 5)
    pwr_set = utils.powerset([(i + 1) for i in range(vrp.nodes_count - 1)])
    for subset in pwr_set:
        if len(subset) > 0:
            solver.Add(sum([edge_vars[var_key] for var_key in edge_vars if var_key[0] not in subset and var_key[1] in subset]) >= 1)

    # Objective function
    solver.Minimize(sum([edge_vars[var_key] * vrp.dist(var_key[0], var_key[1]) for var_key in edge_vars]))

    status = solver.Solve()

    # Get solution if exists
    if status != pywraplp.Solver.OPTIMAL:
        raise SystemError('Solution does not exists')

    successors = {}
    for var_key in edge_vars:
        edge_var = edge_vars[var_key]
        value = edge_var.solution_value()
        
        if value:
            if successors.get(var_key[0]) is None: successors[var_key[0]] = []
            successors[var_key[0]].append(var_key[1])

    vrp.rides = []
    for succ in successors[vrp.depot_node]:
        ride_nodes = [vrp.depot_node]
        ride_nodes.append(succ)
        while succ != vrp.depot_node:
            succ = successors[succ][0]
            ride_nodes.append(succ)
        vrp.rides.append(Ride(0, ride_nodes))

    return vrp