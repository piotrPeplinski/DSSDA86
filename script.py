import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

data_folder = Path(__file__).resolve().parent / 'data'

df = pd.read_csv(data_folder / 'data.csv')
print(df)
df['Revenue'] = df['Price']*df['Quantity']

# products = df.groupby('Product')['Revenue'].sum().reset_index()

# chart = plt.pie(products['Revenue'], labels=products['Product'])
# plt.show()

#wykres x (poziom) - data, y (pion) - przychody