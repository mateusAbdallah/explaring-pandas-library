# %% 

import pandas as pd

# %%

df = pd.read_excel('../data/transactions.xlsx')
df

# %%

df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()

# %%

        