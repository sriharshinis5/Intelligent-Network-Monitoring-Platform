import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/network_logs.csv")

plt.figure(figsize=(8,5))
plt.plot(data["Latency"])
plt.title("Network Latency Analysis")
plt.xlabel("Sample")
plt.ylabel("Latency (ms)")
plt.grid()

plt.savefig("results/traffic_analysis.png")

print("Graph saved.")
