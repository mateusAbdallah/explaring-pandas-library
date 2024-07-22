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

# %%

import datetime

date1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - date1).days

# %%

def recencia (x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
    .agg({"Points": "sum",
          "UUID": "count",
          "DtTransaction": ["max", recencia]
          })
    .rename(columns={"Points": "Value",
                     "UUID": "Frequency",
                     "DtTransaction": "Last_Date"})      
    .reset_index()
)   