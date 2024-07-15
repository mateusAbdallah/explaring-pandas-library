# %% 

import pandas as pd

# %%

df = pd.read_excel('../data/transactions.xlsx')
df

# %%

df_summary = df.groupby(['IdCustomer'])['Points'].sum()
df_summary.reset_index()

# %%

df_agg = (df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={"Points": "Value",
                     "UUID": "Frequency",
                     "DtTransaction": "Last_Date"})      
    .reset_index()
)   

df_agg
