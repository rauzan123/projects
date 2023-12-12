# Using and understanding Numpy (Numeric Python)

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]
# Import the numpy package as np
import numpy as np
# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(type(np_baseball))

# height_in is available as a regular list

# heigth_in variable from mlb players
height_in = [74, 74, 72, 75, 75, 73, 68, 70, 60, 80]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)
# Print out np_height_in
print(np_height_in)
# Convert np_height_in to m: np_height_m
# convert height from inches to meters 
np_height_m = np_height_in * 0.0254
print("Height in meter : " + str(np_height_m))

weight_lb = [180, 215, 210, 205, 190, 195, 160, 175, 170, 270]
print(weight_lb)
# Create array from weight_lb with metric units: np_weight_kg
np_weight_lb = np.array(weight_lb)
# convert lbs into  kilograms
np_weight_kg = np_weight_lb * 0.453592
print("Weight in kg : " + str(np_weight_kg))
# Calculate the BMI: bmi
bmi = np_weight_kg/np_height_m **2
print("Body Mass Index : " + str(bmi))

# Create the light array
light = bmi < 26
# Print out light
print(light)
# Print out BMIs of all baseball players whose BMI is below 30
print("Data yang < 26 : " + str(bmi[light]))

# np.array([True, 1, 2]) + np.array([3, 4, False]) menghasilkan array[4, 5, 2]
# karna True = 1 dan False = 0

#subsetting numpy arrays
print("Data ke 3 : " + str(np_weight_lb[2]))
print(np_height_in[2:6])

baseball_2 = [[180, 78.4],
              [215, 102.7],
              [210, 98.5],
              [188, 75.2]]

np_baseball_2 = np.array(baseball_2)
# Print out the type of np_baseball
print(type(np_baseball_2))
# Print out the shape of np_baseball
print(np_baseball_2.shape)

#numpy arithmetic
import numpy as np
football = [[74, 180, 25],
            [75, 215, 26],
            [73, 210, 21],
            [80, 270, 33],
            [60, 170, 18],
            [76, 186, 24],
            [68, 176, 22],
            [82, 240, 29],
            [79, 210, 31]]
np_football = np.array(football)
print(np_football * 2)
conversion = np_football * np.array([0.0254, 0.453592, 1])
print("Dalam Meter dan Kg :                                                                 " + str(conversion))

#find mean and median in numpy
np_height_football = conversion[:,0]
print(np_height_football)
mean_football = np.mean(np_height_football)
median_football = np.median(np_height_football)
print("Mean : " + str(mean_football))
print("Median : " + str(median_football))

# mencari std dan korelasi dari sebuah array
stdev = np.std(np_height_football)
print("Standard deviasi : "+str(stdev))
corr = np.corrcoef(np_football[:,0], np_football[:,1])
print("Correlation : "+str(corr))










            

