# %%

import pandas as pd

# %%
 
df = pd.read_excel('../data/transactions.xlsx')
df


# %%
# getting the last transaction of each customer

df = (df.sort_values('DtTransaction', ascending=False)
    .drop_duplicates(subset=['IdCustomer'])) 
df

