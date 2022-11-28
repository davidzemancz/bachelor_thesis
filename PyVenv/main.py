from vrp import VRP,Ride,Vehicle,Order
import vrp_drawer
import vrp_solver

vrp = VRP(0, 13)
vrp.vehicles = [
    Vehicle(1, 3, 12),
    Vehicle(2, 5, 22),
    Vehicle(3, 8, 36),
]
vrp.orders = [
    Order(1, 1, 3),
    Order(2, 2, 2),
    Order(3, 3, 1),
    Order(4, 4, 1),
    Order(5, 5, 4),
    Order(6, 6, 5),
    Order(7, 7, 1),
    Order(8, 8, 3),
    Order(9, 9, 5),
    Order(10, 10, 1),
    Order(11, 11, 3),
    Order(12, 12, 3),
]
vrp.rides = [
    Ride(vrp.vehicle(1),[vrp.depot_node, 1,10,12, vrp.depot_node]),
    Ride(vrp.vehicle(2),[vrp.depot_node, 2,4,5,6,8, vrp.depot_node]),
    Ride(vrp.vehicle(3),[vrp.depot_node, 3,7,9,11, vrp.depot_node]),
]

solverd_vrp = vrp_solver.solve_ortools(vrp)
vrp_drawer.draw(solverd_vrp)
