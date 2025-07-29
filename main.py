import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data={
    "Time(seconds)":[0,1,2,3,4,5],
    "Velocity(m/s)":[0,2,4,6,8,10]
}
df=pd.DataFrame(data)
sns.set(style="whitegrid")
plt.figure(figsize=(8,5))
sns.lineplot(x="Time(seconds)",y="Velocity(m/s)",data=df,marker="o")
plt.title("Time vs Velocity")
plt.xlabel("Time(seconds)")
plt.ylabel("Velocity(m/s)")
plt.show()