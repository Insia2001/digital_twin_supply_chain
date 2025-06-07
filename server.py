# server.py

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule, NetworkModule
from model import SupplyChainModel

def network_portrayal(G):
    portrayal = {"nodes": [], "links": []}
    for node_id, data in G.nodes(data=True):
        agents = data.get("agent", [])
        if agents:
            agent = agents[0]
            color = {
                "SupplierAgent": "green",
                "ManufacturerAgent": "blue",
                "RetailerAgent": "orange",
                "TransportAgent": "gray"
            }.get(agent.__class__.__name__, "black")
            portrayal["nodes"].append({
                "id": node_id,
                "color": color,
                "size": 12,
                "tooltip": f"{agent.__class__.__name__} {agent.unique_id}"
            })
    for source, target in G.edges():
        portrayal["links"].append({"source": source, "target": target})
    return portrayal

# The three series must exactly match your DataCollector keys
chart = ChartModule(
    [
        {"Label": "Supplier_Capacity",      "Color": "Green"},
        {"Label": "Manufacturer_Inventory", "Color": "Blue"},
        {"Label": "Retailer_Stock",         "Color": "Orange"},
    ],
    data_collector_name='datacollector'
)

network = NetworkModule(network_portrayal, 500, 500)

server = ModularServer(
    SupplyChainModel,
    [network, chart],
    "Supply Chain Digital Twin",
    {}  # no extra parameters
)
server.port = 8521
server.launch()
