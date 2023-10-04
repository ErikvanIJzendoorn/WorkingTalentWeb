print('Starting program...')

import pandas as pd

df = pd.read_csv('pokemon.csv')

# print(df["Name"])

for index, rij in df.iterrows():
    print(index, rij["Name"], rij['Attack'])