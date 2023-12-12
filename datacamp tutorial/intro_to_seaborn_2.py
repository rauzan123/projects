import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

student_alcohol_consumption = pd.read_csv(r'C:\Users\LENOVO\Downloads\student-alcohol-consumption.csv')
print(student_alcohol_consumption.head())

young_people_survey = pd.read_csv(r'C:\Users\LENOVO\Downloads\young-people-survey-responses.csv')
print(young_people_survey.head())

# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", kind='scatter',
                data=student_alcohol_consumption)

# Show plot
plt.show()


# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_alcohol_consumption,
            col='study_time',
            kind="scatter")
            
# Show plot
plt.show()


# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_alcohol_consumption,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()


# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', 
            data=student_alcohol_consumption, 
            kind='scatter')

# Show plot
plt.show()


# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            col='schoolsup',    
            data=student_alcohol_consumption, 
            col_order=['yes', 'no'],
            kind="scatter")

# Show plot
plt.show()


# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_alcohol_consumption,
            kind="scatter", 
            col="schoolsup",
            row='famsup',
            row_order=["yes", "no"], 
            col_order=['yes', 'no'])

# Show plot
plt.show()


mpg = pd.read_csv(r'C:\Users\LENOVO\Downloads\mpg.csv')
print(mpg.head())


# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, 
            kind='scatter', size="cylinders")

# Show plot
plt.show()


# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", hue='cylinders',
            size="cylinders")

# Show plot
plt.show()


# Create a scatter plot of acceleration vs. mpg
sns.relplot(x="acceleration", y="mpg", 
            data=mpg, kind='scatter', 
            hue='origin', style='origin')

# Show plot
plt.show()


# Create line plot
sns.relplot(x="model_year", y='mpg', 
            data=mpg, kind='line')

# Show plot
plt.show()


# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            ci="sd",
            data=mpg, kind="line")

# Show plot
plt.show()


# Create line plot of model year vs. horsepower
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, ci=None, kind='line')

# Show plot
plt.show()


# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", hue='origin',
            data=mpg, kind="line", style='origin',
            ci=None)

# Show plot
plt.show()


# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", dashes=False,
            ci=None, style="origin", markers=True,
            hue="origin")

# Show plot
plt.show()
