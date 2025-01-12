import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df['day'] = pd.to_datetime(df['Date'], format='%m/%d/%y')

df["Z-score"] = pd.to_numeric(df["Z-score"], errors="coerce") 

plt.figure(figsize=(12, 6))
sns.scatterplot(
    x=df['day'], 
    y=df["Z-score"], 
    hue=abs(df["Z-score"]) > 1.5, 
    palette={False: "blue", True: "red"},
    s=100
)

plt.axhline(0, color="green", linestyle="--", label="Z-score = 0")

plt.axhline(1.5, color="orange", linestyle="--", label="Upper Threshold (Z = 1.5)")
plt.axhline(-1.5, color="orange", linestyle="--", label="Lower Threshold (Z = -1.5)")

plt.title("Z-Score Analysis Over Time")
plt.xlabel("Date")
plt.ylabel("Z-score")
plt.legend(title="Anomaly")
plt.xticks(rotation=45)  
plt.tight_layout()
plt.show()
