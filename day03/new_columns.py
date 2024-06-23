# %%

import pandas as pd

df = pd.read_csv('../data/customers.csv', sep=';')


# %%

df['Points_double'] = df['Points'] * 2
df
