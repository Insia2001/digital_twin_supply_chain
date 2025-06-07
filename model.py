# supply_chain_model/model.py

from mesa import Model
from mesa.datacollection import DataCollector
from mesa.time import SimultaneousActivation
from mesa.space import NetworkGrid
import networkx as nx

from agent import SupplierAgent, ManufacturerAgent, RetailerAgent, TransportAgent


class SupplyChainModel(Model):
    def __init__(self, num_steps=10):
        super().__init__()
        self.num_steps = num_steps
        # Scheduler
        self.schedule = SimultaneousActivation(self)
        # Network graph
        self.G = nx.DiGraph()
        self.G.add_nodes_from([1, 2, 3, 4])
        self.G.add_edges_from([
            (1, 2),  # Supplier -> Manufacturer
            (2, 3),  # Manufacturer -> Retailer
            (2, 4)   # Manufacturer -> Transport
        ])
        # Initialize agent lists on nodes
        for node in self.G.nodes:
            self.G.nodes[node]["agent"] = []
        # Grid based on graph
        self.grid = NetworkGrid(self.G)

        # Instantiate agents
        self.supplier = SupplierAgent(1, self, capacity=100)
        self.manufacturer = ManufacturerAgent(2, self, demand=50, production_capacity=60)
        self.retailer = RetailerAgent(3, self, demand=30)
        self.transport = TransportAgent(4, self, reliability=0.9)

        # Place agents in grid
        self.grid.place_agent(self.supplier, 1)
        self.grid.place_agent(self.manufacturer, 2)
        self.grid.place_agent(self.retailer, 3)
        self.grid.place_agent(self.transport, 4)

        # Add agents to schedule
        for agent in [self.supplier, self.manufacturer, self.retailer, self.transport]:
            self.schedule.add(agent)

        # Data collector for model-level metrics
        self.datacollector = DataCollector(
            model_reporters={
                "Supplier_Capacity":      lambda m: m.supplier.capacity,
                "Manufacturer_Inventory": lambda m: m.manufacturer.inventory,
                "Retailer_Stock":         lambda m: m.retailer.stock,
            }
        )

    def step(self):
        # Collect data before stepping
        self.datacollector.collect(self)
        # Advance the model by one step
        self.schedule.step()
