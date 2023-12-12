import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

countries = pd.read_csv(r'C:\Users\LENOVO\Downloads\countries-of-the-world.csv')
print(countries.head())

gdp = countries["GDP ($ per capita)"]
print(gdp.head())

phones = countries["Phones (per 1000)"]
print(phones.head())

percent_literate = countries["Literacy (%)"]
print(percent_literate.head())

region = countries["Region"]
print(region.head())


# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)
plt.show()


# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()


student_alcohol_consumption = pd.read_csv(r'C:\Users\LENOVO\Downloads\student-alcohol-consumption.csv')
print(student_alcohol_consumption.head())

young_people_survey = pd.read_csv(r'C:\Users\LENOVO\Downloads\young-people-survey-responses.csv')
print(young_people_survey.head())


# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=young_people_survey)

# Display the plot
plt.show()


# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", 
                data=student_alcohol_consumption, 
                hue="location", 
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()


# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups
sns.countplot(x="school", 
            data=student_alcohol_consumption, 
            hue="location", palette=palette_colors)

# Display plot
plt.show()


