
DEPOT_NODE = 0
UNDEF_NODE = -1



class Vehicle:
    NONE = None

    def __init__(self, id, capacity, charge):
        self.id = id
        self.capacity = capacity
        self.charge = charge
        self.speed = 0

class Order:
    NONE = None

    def __init(self, id, node, demand):
        self.id = id
        self.node = node
        self.demand = demand

class Ride:
    def __init__(self, vehicle, nodes):
        self.vehicle = vehicle
        self.nodes = nodes

class Delivery:
    def __init__(self, order):
        self.order = order

class VRP:
    def __init__(self, nodes):
        self.nodes = nodes
        self.vehicles = []
        self.orders = []

        self.deliveries = []
        self.rides = []

    def vehicle(self, vehicleId) -> Vehicle:
        for v in self.vehicles:
            if v.id == vehicleId: return v
        raise KeyError(vehicleId)

    def order(self, orderId) -> Order:
        for o in self.orders:
            if o.id == orderId: return o
        raise KeyError(orderId)