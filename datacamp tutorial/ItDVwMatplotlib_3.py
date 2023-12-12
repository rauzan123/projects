from email.mime.base import MIMEBase
import matplotlib.pyplot as plt
import pandas as pd

medals = pd.read_csv(r'C:\Users\LENOVO\Downloads\medals_by_country_2016.csv', index_col=0)
print(medals)

# BAR TYPE
fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.barh(medals.index, 
        medals['Gold'], color='gold', 
        align='center')

# Set the x-axis tick labels to the country names
x1 = [0, 20, 40, 60, 80, 100, 120, 140]
number = [0, 20, 40, 60, 80, 100, 120, 140]
ax.set_xticks(x1)
ax.set_xticklabels(number)

# Set the y-axis label
plt.show()


# Add bars for "Gold" with the label "Gold"
fig, ax = plt.subplots()

ax.bar(medals.index, medals['Gold'], 
      label="Gold", color='gold')

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals['Silver'], 
      bottom=medals['Gold'], label='Silver', 
      color='silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], 
      bottom=medals['Gold'] + medals['Silver'], 
      label='Bronze', color='saddlebrown')

ax.set_xticklabels(medals.index, rotation=90)
# Display the legend
ax.legend()

plt.show()


olympic_2016 = pd.read_csv(r'C:\Users\LENOVO\Downloads\summer2016.csv')
print(olympic_2016)

mens_rowing = olympic_2016[olympic_2016['Sport'] == 'Rowing']
print(mens_rowing)

mens_gymnastics = olympic_2016[olympic_2016['Sport'] == 'Gymnastics']
print(mens_gymnastics)

# HISTOGRAM TYPE
fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()


fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'], histtype='step', 
        bins=5, label="Rowing")

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'],histtype='step',
        bins=5, label="Gymnastics")

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend(loc='upper left')
plt.show()

# ERROR TYPE
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), 
        yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(),
       yerr=mens_gymnastics["Height"].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()


# BOXPLOT TYPE
fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], 
            mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(["Rowing", "Gymnastics"])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()


# Extract the "Sport" column
sports_column = olympic_2016['Sport']

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)


fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports :
  # Extract the rows only for this sport
  sport_df = olympic_2016[olympic_2016['Sport']== sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df['Weight'].mean(), 
          yerr=sport_df['Weight'].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig(r'C:\Users\LENOVO\Downloads\sports_weights.png')




