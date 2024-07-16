import pandas as pd
from datetime import datetime

url = "https://raw.githubusercontent.com/LokeshKumarChauhan/DE_with_powerBI/main/Walmart.csv"

df = pd.read_csv(url)

df['Order ID'] = df['Order ID'].astype('string')
df['Order Date'] = df['Order Date'].astype('datetime64[ns]')
df['Ship Date'] = df['Ship Date'].astype('datetime64[ns]')
df['Ship Mode'] = df['Ship Mode'].astype('string')
df['Ship Mode'] = df['Ship Mode'].astype('string')
df['Customer ID'] = df['Customer ID'].astype('string')
df['Customer Name'] = df['Customer Name'].astype('string')
df['Segment'] = df['Segment'].astype('string')
df['Country'] = df['Country'].astype('string')
df['City'] = df['City'].astype('string')
df['State'] = df['State'].astype('string')
df['Region'] = df['Region'].astype('string')
df['Category'] = df['Category'].astype('string')
df=df.rename(columns={'Sub-Category' : 'Sub Category'})
df['Sub Category'] = df['Sub Category'].astype('string')
df['Product Name'] = df['Product Name'].astype('string')

df['Order Date'].dt.date
df['Ship Date'].dt.date

df = df.sort_values(by='Ship Date')
df = df.sort_values(by='Order Date')


df.to_csv('processed_sales.csv')
