import pandas as pd
sales = pd.read_csv("Downloads\walmart sales - sales_subset.csv", index_col=0)
print(sales.head())
print(sales.tail())
# Print the info about the sales DataFrame
print(sales.info())
print("total number of data :" , len(sales))
# Print the mean of weekly_sales
print("  mean weekly sales :", sales["weekly_sales"].mean())
# Print the median of weekly_sales
print("  median weekly sales :", sales["weekly_sales"].median())

# Print the maximum of the date column
print("  data sales terbaru :", sales["date"].max())
# Print the minimum of the date column
print("  data sales pertama/terlama :", sales["date"].min())

# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print("  Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment :")
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))


sales_1_1 = sales[(sales["store"] == 1)
& (sales["department"] == 1)]
print("  data sales_1_1 :")
print(sales_1_1)

# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date", ascending=True)
# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1["weekly_sales"].cumsum()
# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1["weekly_sales"].cummax()
# See the columns you calculated
print("  data sales yg cumulative :")
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])


# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset =["store", "type"])
print("  sales drop duplicates store&type :")
print(store_types.head())
# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset =["store", "department"])
print("  Drop duplicate store/department combinations :")
print(store_depts)
# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"] == True].drop_duplicates(subset="date")
# Print date col of holiday_dates
print("  Subset the rows where is_holiday is True and drop duplicate dates :")
print(holiday_dates)

# Count the number of stores of each type
store_counts = store_types["type"].value_counts()
print("  Count the number of stores of each type :")
print(store_counts)
# Get the proportion of stores of each type
store_props = store_types["type"].value_counts(normalize=True)
print("  Get the proportion of stores of each type :")
print(store_props)
# Count the number of each department number and sort
dept_counts_sorted = store_depts["department"].value_counts(sort=True)
print("  Count the number of each department number and sort :")
print(dept_counts_sorted)
# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts["department"].value_counts(sort=True, normalize=True)
print("  Get the proportion of departments of each number and sort :")
print(dept_props_sorted)


# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()
print(" jlh all type sales :", sales_all)
# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
print(" jlh sales A :",sales_A)
# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
print(" jlh sales B :",sales_B)
# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print("sales type proportion :", sales_propn_by_type)

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
print("  Group by type; calc total weekly sales :")
print(sales_by_type)
# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print("  Get proportion for each type :")
print(sales_propn_by_type)
# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print("  Group by type and is_holiday; calc total weekly sales :")
print(sales_by_type_is_holiday)

# Import numpy with the alias np
import numpy as np
# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])
# Print sales_stats
print("  Print sales_stats :")
print(sales_stats)
# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])
# Print unemp_fuel_stats
print("  Print unemp_fuel_stats :")
print(unemp_fuel_stats)


# Pivot for mean weekly_sales for each store type
import numpy as np
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")
# Print mean_sales_by_type
print("  Print mean_sales_by_type :")
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=[np.mean, np.median])
# Print mean_med_sales_by_type
print("  Print mean_med_sales_by_type :")
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index="type", columns="is_holiday")
# Print mean_sales_by_type_holiday
print("  Print mean_sales_by_type_holiday :")
print(mean_sales_by_type_holiday)

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print("Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols :")
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))












