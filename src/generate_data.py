import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = pd.DataFrame({
    "Latency": np.random.normal(15,5,rows),
    "PacketLoss": np.random.normal(0.5,0.2,rows),
    "Throughput": np.random.normal(90,10,rows),
    "BandwidthUsage": np.random.normal(50,15,rows)
})

data["Label"] = 0

anomaly_index = np.random.choice(rows,100)

data.loc[anomaly_index,"Latency"] = np.random.normal(70,10,100)
data.loc[anomaly_index,"PacketLoss"] = np.random.normal(8,2,100)
data.loc[anomaly_index,"Label"] = 1

data.to_csv("network_logs.csv",index=False)

print("Dataset Generated")
