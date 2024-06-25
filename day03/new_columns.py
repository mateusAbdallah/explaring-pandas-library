# %%

import pandas as pd

df = pd.read_csv('../data/customers.csv', sep=';')


# %%

df['Points_double'] = df['Points'] * 2
df

# %%

#get the first name after split based on underscore
def get_first(nome:str):
    return nome.split("_")[0]

# %%

df['first_name'] = df['Name'].apply(get_first)
df

# %%
#another way to apply function
df['Name'].apply(lambda x: x.upper().split('_')[0])