import pandas as pd
import numpy as np

data = pd.read_csv('Data/raw_data/thyroid_data.csv')

data.age = data.age.replace(['?'], np.nan)
data.age = data.age.astype(float)
# print(round(data['age'].mean(),2))


pos = data.age.mean() + (2.5*data.age.std())
print(pos)

neg = data.age.mean() - (2.5*data.age.std())
print(neg)

print()

pos = data.age.mean() + (3*data.age.std())
print(pos)

neg = data.age.mean() - (3*data.age.std())
print(neg)