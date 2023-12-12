import pandas as pd

employees = pd.read_csv(r'C:\Users\LENOVO\Downloads\employees - Sheet2 (1).csv')
print(employees)

top_cust = pd.read_csv(r'C:\Users\LENOVO\Downloads\top customer - Sheet3.csv')
print(top_cust)

empl_cust = employees.merge(top_cust, on='srid', 
            how='left', indicator=True)
print(empl_cust)
# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']
print(srid_list)
# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])









