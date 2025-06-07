# supply_chain_model/agent.py
from mesa import Agent
import random

class SupplierAgent(Agent):
    def __init__(self, unique_id, model, capacity):
        super().__init__(unique_id, model)
        self.capacity = capacity
        self.operational = True

    def step(self):
        # Simulate random failure (10% chance)
        if random.random() < 0.1:
            self.operational = False
            print(f"Supplier {self.unique_id} failed this step.")
        else:
            self.operational = True
            print(f"Supplier {self.unique_id} is operational.")
class ManufacturerAgent(Agent):
    def __init__(self, unique_id, model, demand, production_capacity):
        super().__init__(unique_id, model)
        self.demand = demand
        self.production_capacity = production_capacity
        self.inventory = 0
        self.risk_factor = 0.05  # Optional: risk of disruption

    def step(self):
        # Simulate risk
        if random.random() < self.risk_factor:
            print(f"Manufacturer {self.unique_id} disrupted! No production.")
            return

        # Collect supplies (simplified logic)
        total_supplies = 0
        for neighbor_id in self.model.G.predecessors(self.pos):
            supplier = self.model.grid.get_cell_list_contents([neighbor_id])[0]
            if isinstance(supplier, SupplierAgent) and supplier.operational and supplier.capacity > 0:
                supply = min(supplier.capacity, self.production_capacity - total_supplies)
                supplier.capacity -= supply
                total_supplies += supply
                print(f"Manufacturer {self.unique_id} received {supply} units from Supplier {supplier.unique_id}.")
                if total_supplies >= self.production_capacity:
                    break

        self.inventory += total_supplies
        print(f"Manufacturer {self.unique_id} inventory after production: {self.inventory}")

class RetailerAgent(Agent):
    def __init__(self, unique_id, model, demand):
        super().__init__(unique_id, model)
        self.demand = demand
        self.stock = 0

    def step(self):
        # Attempt to get goods from manufacturer
        for neighbor_id in self.model.G.predecessors(self.pos):
            manufacturer = self.model.grid.get_cell_list_contents([neighbor_id])[0]
            if isinstance(manufacturer, ManufacturerAgent) and manufacturer.inventory >= 10:
                manufacturer.inventory -= 10
                self.stock += 10
                print(f"Retailer {self.unique_id} received 10 units from Manufacturer {manufacturer.unique_id}.")

        print(f"Retailer {self.unique_id} stock: {self.stock}")

class TransportAgent(Agent):
    def __init__(self, unique_id, model, reliability):
        super().__init__(unique_id, model)
        self.reliability = reliability

    def step(self):
        # Could later be used to simulate delayed deliveries
        if random.random() > self.reliability:
            print(f"TransportAgent {self.unique_id} caused a delay!")
        else:
            print(f"TransportAgent {self.unique_id} operating normally.")
