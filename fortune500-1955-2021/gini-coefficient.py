import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fortune500.csv')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

def gini(x):
    n = len(x)
    y = sorted(x)
    return sum((2 * i - n  - 1) * y_i for i, y_i in enumerate(y, 1)) / (n * sum(y))   

gini_by_year = df.groupby('Year')['Revenue'].apply(gini)

plt.figure(figsize=(10, 6))
gini_by_year.plot()
plt.title('Gini Coefficient Over Time')
plt.xlabel('Year')
plt.ylabel('Gini Coefficient')
plt.grid(True)
plt.show()