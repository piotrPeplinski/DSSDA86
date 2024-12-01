import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

data_folder = Path(__file__).resolve().parent / 'data'

df = pd.read_csv(data_folder / 'salaries.csv')

df['Date_Of_Payment'] = pd.to_datetime(df['Date_Of_Payment'])

poland_2016 = df[(df['Date_Of_Payment'].dt.year == 2016)
                 & (df['Country'] == 'Poland')]

monthly_expenses = poland_2016.groupby(poland_2016['Date_Of_Payment'].dt.strftime('%B'))[
    'Monthly_Salary'].sum().reset_index()

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

monthly_expenses['Date_Of_Payment'] = pd.Categorical(
    monthly_expenses['Date_Of_Payment'],
    categories=month_order,
    ordered=True
)

monthly_expenses = monthly_expenses.sort_values('Date_Of_Payment')

plt.figure(figsize=(10,6))
plt.bar(monthly_expenses['Date_Of_Payment'],monthly_expenses['Monthly_Salary'])
plt.xticks(rotation=45)
plt.show()