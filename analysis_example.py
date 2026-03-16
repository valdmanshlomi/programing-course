import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("prices.csv")

df.columns = df.columns.str.strip()

print(df)

plt.plot(df["price"])

plt.title("Price chart")
plt.xlabel("Time")
plt.ylabel("Price")

plt.show()
