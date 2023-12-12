# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()

import pandas as pd

seattle_weather_ungrouped = pd.read_csv(r'C:\Users\LENOVO\Downloads\seattle_weather.csv')
print(seattle_weather_ungrouped)
print(seattle_weather_ungrouped.info())
seattle_weather_ungrouped['MONTH'] = pd.to_datetime(seattle_weather_ungrouped['DATE'], format='%m').dt.month_name().str.slice(stop=3)

austin_weather = pd.read_csv(r'C:\Users\LENOVO\Downloads\austin_weather.csv')
print(austin_weather)
print(austin_weather.info())
austin_weather['MONTH'] = pd.to_datetime(austin_weather['DATE'], format='%m').dt.month_name().str.slice(stop=3)

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

seattle_weather = seattle_weather_ungrouped[seattle_weather_ungrouped['STATION'] == 'USW00094290']
print(seattle_weather)
# Plot MLY-PRCP-NORMAL from seattle_weather against MONTH
ax.plot(seattle_weather["MONTH"], 
        seattle_weather["MLY-PRCP-NORMAL"])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather["MONTH"], 
        austin_weather["MLY-PRCP-NORMAL"])

plt.legend(["seattle", "austin"])
# Call the show function
plt.show()


# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()
# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"],
        seattle_weather["MLY-PRCP-NORMAL"], 
        color='b', marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], 
        austin_weather["MLY-PRCP-NORMAL"], 
        color='r', marker='v', linestyle='--')

# Call show to display the resulting plot
plt.legend(["seattle", "austin"])
plt.show()



# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], 
        seattle_weather["MLY-PRCP-NORMAL"])
ax.plot(austin_weather["MONTH"], 
        austin_weather["MLY-PRCP-NORMAL"])

# Customize the x-axis label
ax.set_xlabel("Time (months)")

# Customize the y-axis label
ax.set_ylabel("Precipitation (inches)")

# Add the title
ax.set_title("Weather patterns in Austin and Seattle")

# Display the figure
plt.legend(["seattle", "austin"])
plt.show()



# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'], 
                seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], 
                seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1, 0].plot(austin_weather['MONTH'], 
                austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1, 1].plot(austin_weather['MONTH'], 
                austin_weather["MLY-TAVG-NORMAL"])
plt.show()


# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather["MONTH"], 
            seattle_weather["MLY-PRCP-NORMAL"], 
            color = 'b')
ax[0].plot(seattle_weather["MONTH"], 
            seattle_weather["MLY-PRCP-25PCTL"], 
            color = 'b', linestyle = '--')
ax[0].plot(seattle_weather["MONTH"], 
            seattle_weather["MLY-PRCP-75PCTL"], 
            color = 'b', linestyle = '--')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather["MONTH"], 
            austin_weather["MLY-PRCP-NORMAL"], 
            color = 'r')
ax[1].plot(austin_weather["MONTH"], 
            austin_weather["MLY-PRCP-25PCTL"], 
            color = 'r', linestyle='--')
ax[1].plot(austin_weather["MONTH"], 
            austin_weather["MLY-PRCP-75PCTL"], 
            color = 'r', linestyle='--')

plt.show()


fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather['MONTH'], 
            seattle_weather["MLY-TAVG-NORMAL"], 
            yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], 
            austin_weather["MLY-TAVG-NORMAL"], 
            yerr=austin_weather["MLY-TAVG-STDDEV"])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()


# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], 
        seattle_weather["MLY-TAVG-NORMAL"])
plt.show()


# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], 
        austin_weather["MLY-TAVG-NORMAL"])
plt.show()
fig.set_size_inches([5, 3])
fig.savefig(r'C:\Users\LENOVO\Downloads\Solarize_light.png')











