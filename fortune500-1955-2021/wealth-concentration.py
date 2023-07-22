import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fortune500.csv')
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

total_revenue_by_year = df.groupby('Year')['Revenue'].sum()
top_1_share_by_year = df[df['Rank'] == 1].groupby('Year')['Revenue'].sum() / total_revenue_by_year
top_5_share_by_year = df[df['Rank'] <= 5].groupby('Year')['Revenue'].sum() / total_revenue_by_year
top_10_share_by_year = df[df['Rank'] <= 10].groupby('Year')['Revenue'].sum() / total_revenue_by_year
top_50_share_by_year = df[df['Rank'] <= 50].groupby('Year')['Revenue'].sum() / total_revenue_by_year
plt.plot(top_1_share_by_year.index, top_1_share_by_year.values, label='Top 1')
plt.plot(top_5_share_by_year.index, top_5_share_by_year.values, label='Top 5')
plt.plot(top_10_share_by_year.index, top_10_share_by_year.values, label='Top 10')
plt.plot(top_50_share_by_year.index, top_50_share_by_year.values, label='Top 50')
plt.legend()
plt.title('Revenue Concentration Over Time')
plt.xlabel('Year')
plt.ylabel('Share of Total Revenue')
plt.grid(True)
plt.show()

