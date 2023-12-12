
from cmath import pi
from flask import g
import pandas as pd

sp500 = pd.read_csv(r'C:\Users\LENOVO\Downloads\S&P500.csv')
print(sp500)

gdp = pd.read_csv(r'C:\Users\LENOVO\Downloads\WorldBank_GDP.csv')
print(gdp)

# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='Year', 
                            right_on='Date', 
                             how='left')
# Print gdp_sp500
print(gdp_sp500)
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, 
                            fill_method='ffill', 
                            left_on='Year', 
                            right_on='Date', how='left')
# Print gdp_sp500
print (gdp_sp500)
# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['GDP','Returns']]
# Print gdp_returns correlation
print(gdp_returns.corr())


unemployment = pd.read_csv(r'C:\Users\LENOVO\Downloads\Unemployment rate - unemployment.csv')
print(unemployment)

inflation = pd.read_csv(r'C:\Users\LENOVO\Downloads\cpi - cpi.csv')
print(inflation)

import matplotlib.pyplot as plt

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, 
                                    unemployment, 
                                    on='date', 
                                    how='inner')
# Print inflation_unemploy 
print(inflation_unemploy)
# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(x="unemployment_rate", 
                        y="cpi", kind="scatter")
plt.show()


pop = pd.read_csv(r'C:\Users\LENOVO\Downloads\WorldBank_POP.csv')
print(pop)
# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, 
                            on=['Year','Country Name'], 
                             fill_method='ffill')
# Print ctry_date
print(ctry_date)

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['Country Name', 'Year'], fill_method='ffill')
# Print date_ctry
print(date_ctry)

jpm = pd.read_csv(r'C:\Users\LENOVO\Downloads\jp morgan - jp morgan stocks (1).csv')
jpm["date_time"] = pd.to_datetime(jpm["date_time"])
print(jpm)


wells = pd.read_csv(r'C:\Users\LENOVO\Downloads\wells stocks - wells stocks.csv')
wells["date_time"] = pd.to_datetime(wells["date_time"])
print(wells)

bac = pd.read_csv(r'C:\Users\LENOVO\Downloads\bac  - bac stocks.csv')
bac["date_time"] = pd.to_datetime(bac["date_time"])
print(bac)


# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm, wells, on='date_time', 
                          suffixes=('', '_wells'), 
                          direction='nearest')
print(jpm_wells)

# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells, bac, 
                                on='date_time', 
                              suffixes=('_jpm', '_bac'), 
                              direction='nearest')
print(jpm_wells_bac)

# Compute price diff
price_diffs = jpm_wells_bac.diff()
print(price_diffs)


# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm','close_wells','close_bac'])
plt.show()


recession = pd.read_csv(r'C:\Users\LENOVO\Downloads\recession - Sheet4.csv')
recession["date"] = pd.to_datetime(recession["date"])
print(recession)

gdp_2 = pd.read_csv(r'C:\Users\LENOVO\Downloads\gdp_2 - Sheet5.csv')
gdp_2["date"] = pd.to_datetime(gdp_2["date"])
print(gdp_2)


# Merge gdp and recession on date using merge_asof()
gdp_recession = pd.merge_asof(gdp_2, recession, on='date')
print(gdp_recession)

# Create a list based on the row value of gdp_recession['econ_status']
is_recession = ['r' if s=='recession' else 'g' for s in gdp_recession['econ_status']]
print(is_recession)

# Plot a bar chart of gdp_recession
gdp_recession.plot(kind='bar', y='gdp', 
                    x='date', color=is_recession, 
                    rot=90)
plt.show()


social_fin = pd.read_csv(r'C:\Users\LENOVO\Downloads\social_financial - Sheet6.csv')
print(social_fin)

print(social_fin.query('value > 50000000'))
print(social_fin.query('financial == "total_revenue" and company == "facebook"'))
print(social_fin.query('financial == "net_income" and value < 0'))
print(social_fin.query('financial == "gross_profit" and value > 100000'))


gdp_3 = pd.read_csv(r'C:\Users\LENOVO\Downloads\gdp_2 - Sheet7 (1).csv')
print(gdp_3)

pop_2 = pd.read_csv(r'C:\Users\LENOVO\Downloads\pop_2 - Sheet8.csv')
print(pop_2)

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp_3, pop_2, 
                            on=['country','date'], 
                            fill_method='ffill')
print(gdp_pop)

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 
                                'date', 'country')
print(gdp_pivot)

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')
print(recent_gdp_pop)

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()


inflation = pd.read_csv(r'C:\Users\LENOVO\Downloads\inflation - Sheet9.csv')
print(inflation)

print(inflation.melt(id_vars=['country','indicator'], 
        var_name='year', value_name='annual'))

