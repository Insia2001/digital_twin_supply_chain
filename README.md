
# Digital Twin of a Supply Chain Using Agent-Based Modeling

This project implements a basic **Digital Twin** of a multi-echelon **Supply Chain** using **Agent-Based Modeling (ABM)** in **Python** with the Mesa framework. The model is designed to simulate the dynamic behavior of supply chain entities (suppliers, manufacturers, warehouses, retailers, and logistics agents) and analyze system performance under various scenarios.

---

##  Overview

- **Framework**: Mesa (Python)
- **Purpose**: To simulate a virtual replica (digital twin) of a supply chain and observe behavior under demand changes, transportation delays, and disruptions.
- **Features**:
  - Autonomous agents (Supplier, Manufacturer, Warehouse, Retailer, Logistics)
  - Inventory management and order fulfillment
  - Dynamic demand and delays
  - Data logging and performance visualization

---

## 📁 Project Structure

```
digital-twin-supply-chain/
- model.py              # Mesa model defining agent logic and simulation
- server.py             # Optional: Mesa visualization server (if used)
- run.py                # Script to run the simulation
- requirements.txt      # Python dependencies
- README.md             # This documentation file
- data/                 # Folder for input/output data (optional)
- results/              # Simulation logs/plots (optional)
```

---

## 🚀 How to Run the Model

### 1. Clone the Repository or Download ZIP
```bash
git clone https://github.com/Insia2001/digital_twin_supply_chain.git
cd digital-twin-supply-chain
```

### 2. Set Up the Environment

Install dependencies using pip:
```bash
pip install -r requirements.txt
```

### 3. Run the Simulation

Basic run (console/logging only):
```bash
python run.py
```

If a Mesa server is included for visualization:
```bash
python server.py
```

---

## 📊 Output

- Logs of order flows, inventory levels, backorders
- Plots of lead times, service levels, or cost metrics
- Scenario-based comparisons (if configured)

---

## 🧩 Agents in the Model

| Agent                | Behavior |
|----------------------|----------|
| **Supplier**         | Manages lead times and sends raw materials |
| **Manufacturer**     | Processes raw materials and produces goods |
| **Warehouse**        | Stores products and fulfills retailer orders |
| **Retailer**         | Places orders based on demand |
| **Logistics**        | Handles transport and simulates delays |

---

## 🧪 Scenarios You Can Simulate

- Sudden spike in customer demand
- Supplier disruption (shutdown, delays)
- Transportation bottlenecks
- Inventory buffer adjustments

---

## 📚 References

- Mesa Documentation: https://mesa.readthedocs.io
- Grieves, M. & Vickers, J. (2017). *Digital Twin in Complex Systems*.
- Macal & North (2010). *Agent-based modeling and simulation*.

---

## 📬 Contact

Author: Insia Fatima Larik
Email: larikinsia@gmail.com 
University: FG Degree College Hyd

---

## 📝 License

This project is for academic use only.
