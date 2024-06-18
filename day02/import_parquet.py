# %%

import pandas as pd

# %%

df_parquet = pd.read_parquet('../data/transactions_cart.parquet')
df_parquet

# %%

df_parquet.head()

# %%

df_parquet.info(memory_usage='deep')