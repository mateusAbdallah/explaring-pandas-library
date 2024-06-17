# %% 

import pandas as pd

# %%
#reading csv file

df_customers = pd.read_csv('../data/customers.csv', sep=';')
df_customers

# %%

df_customers.shape

# %%

df_customers.info(memory_usage='deep')

# %%
df_customers.info()

# %%

df_customers['Points'].astype(int)
 # %%

df_customers.describe()

# %%
# filtering based on certain conditions

condition = df_customers['Points'] > 1500
condition

df_customers[condition]

# %%

condition = df_customers['Points'] == df_customers['Points'].max()
df_max_point = df_customers[condition]
df_max_point

# %%
# rearrange columns

columns = ['Name', 'UUID', 'Points']
df_customers[columns]

# %%

columns = df_customers.columns.tolist()
columns.sort()
# %%

df_customers
# %%

df_customers[columns]
