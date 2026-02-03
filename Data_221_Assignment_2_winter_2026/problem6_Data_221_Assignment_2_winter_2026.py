import pandas as pd

df = pd.read_csv('crime.csv')

df['risk'] = df['ViolentCrimesPerPop'].apply(lambda x: 'High-Crime' if x >= 0.50 else 'LowCrime')

results = df.groupby('risk')['PctUnemployed'].mean()

print("-" * 40)
print("Average Unemployment Rate by Crime Risk:")
print("-" * 40)
print(f"High-Crime Group: {100*results['High-Crime']:.2f}%")
print(f"Low-Crime Group:  {100*results['LowCrime']:.2f}%")