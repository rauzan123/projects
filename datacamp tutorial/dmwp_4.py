import pandas as pd
avocados = pd.read_pickle(r'C:\Users\LENOVO\Downloads\avoplotto.pkl')
print(avocados)


# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Look at the first few rows of data
print(avocados.head())
# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()
# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")
# Show the plot
plt.show()

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()
print(nb_sold_by_date)
# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind="line")
# Show the plot
plt.show()

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")
# Show the plot
plt.show()

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(bins=20, alpha=0.5)
# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(bins=20, alpha=0.5)
# Add a legend
plt.legend(["conventional", "organic"])
# Show the plot
plt.show()


avocados_2016 = pd.read_csv(r"C:\Users\LENOVO\Downloads\avocados_2016 - Sheet1.csv")
print(avocados_2016)

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())
# Check each column for missing values
print(avocados_2016.isna().any())
# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind="bar")
# Show plot
plt.show()

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()
# Check if any columns contain missing values
print(avocados_complete.isna().any())

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()
# Show the plot
plt.show()
# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)
# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()
# Show the plot
plt.show()

