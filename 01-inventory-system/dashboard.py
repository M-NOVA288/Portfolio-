import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("operations.csv")

# Total downtime by month
downtime = df.groupby("month")["downtime_hours"].sum()
downtime.plot(kind="bar", title="Total Downtime by Month")
plt.ylabel("Hours")
plt.show()

# Average maintenance cost
print("Average Maintenance Cost:", df["maintenance_cost"].mean())
