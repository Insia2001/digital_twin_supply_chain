from model import SupplyChainModel

model = SupplyChainModel()

for i in range(10):
    print(f"Step {i + 1}")
    model.step()
