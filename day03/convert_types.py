# %%

import pandas as pd

# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df


# %%
# sorting based on list

# df./sort_values(by=['Points', 'Name'], ascending=[False, True])

# %%
#building a simple pipeline to sort and rename columns

df = (df.sort_values(by=['Points', 'Name'], ascending=[False, True])
    .rename(columns={'UUID':'ID'}))     
df
# %%
