
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

student_alcohol_consumption = pd.read_csv(r'C:\Users\LENOVO\Downloads\student-alcohol-consumption.csv')
print(student_alcohol_consumption.head())

young_people_survey_uncomplete = pd.read_csv(r'C:\Users\LENOVO\Downloads\young-people-survey-responses.csv')
young_people_survey = young_people_survey_uncomplete.dropna()
print(young_people_survey)




# Create count plot of internet usage
sns.catplot(x="Internet usage", data=young_people_survey, 
            kind='count')

# Show plot
plt.show()

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=young_people_survey,
            kind="count")

# Show plot
plt.show()

# Separate into column subplots based on age category
young_people_survey["Age"] = np.where(young_people_survey["Age"] >= 21, "21+", "Less than 21")

sns.catplot(y="Internet usage", 
            data=young_people_survey,col="Age",
            kind="count")

# Show plot
plt.show()


# Create bar plot of average final grade in each study category
sns.catplot(x="study_time", y="G3", 
            data=student_alcohol_consumption, 
            kind='bar')

# Show plot
plt.show()

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3", order=category_order,
            data=student_alcohol_consumption,
            kind="bar")

# Show plot
plt.show()

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3", ci=None,
            data=student_alcohol_consumption,
            kind="bar",
            order=category_order)

# Show plot
plt.show()


# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3", 
            data=student_alcohol_consumption, 
            order=study_time_order, 
            kind='box')

# Show plot
plt.show()


# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", 
            data=student_alcohol_consumption, 
            kind='box', sym="", hue="location")

# Show plot
plt.show()


# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            whis=0.5,
            data=student_alcohol_consumption,
            kind="box")

# Show plot
plt.show()

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_alcohol_consumption,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_alcohol_consumption,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()


# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences", 
            data=student_alcohol_consumption, 
            kind='point')


            
# Show plot
plt.show()

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences", capsize=0.2,
			data=student_alcohol_consumption,
            kind="point")
        
# Show plot
plt.show()

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences", join=False,
			data=student_alcohol_consumption,
            kind="point",
            capsize=0.2)
            
# Show plot
plt.show()


# Create a point plot that uses color to create subgroups
sns.catplot(x="romantic", y="absences", 
            data=student_alcohol_consumption, 
            hue="school", kind='point')

# Show plot
plt.show()

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences", ci=None,
			data=student_alcohol_consumption,
            kind="point",
            hue="school")

# Show plot
plt.show()

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences", estimator=median,
			data=student_alcohol_consumption,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()