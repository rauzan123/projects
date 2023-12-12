# Comparison of booleans
print("apakah True = False :", True == False)
# Comparison of integers
print("apakah operasi ini tidak sama dengan 75 :", -5 * 15 != 75) # != artinya not equal
# Comparison of strings
print("apakah string tsb sama :", "pyscript" == "PyScript")
# Compare a boolean with an integer
print("apakah True = 1 :", True == 1)

# Comparison of integers
x = -3 * 6
print("apakah x lebih besar atau sama dengan -10 :", x>=-10)
# Comparison of strings
y = "test"
print("apakah test lebih kecil atau sama dengan y :", "test"<=y)
# Comparison of booleans
print("apakah True lebih besar dari False :", True > False)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than or equal to 18
print("varibel yg lebih besar atau sama dengan 18 :", my_house >= 18)
# my_house less than your_house
print("varibel yg lebih kecil atau sama dengan your_house :", my_house <= your_house)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# my_kitchen bigger than 10 and smaller than 18?
print("is my_kitchen bigger than 10 and smaller than 18 :", my_kitchen > 10 and my_kitchen < 18)
# my_kitchen smaller than 14 or bigger than 17?
print("is my_kitchen smaller than 14 or bigger than 17 :", my_kitchen < 14 or my_kitchen > 17)
# Double my_kitchen smaller than triple your_kitchen?
print("Double my_kitchen smaller than triple your_kitchen :", 2*my_kitchen < 3*your_kitchen)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# my_house greater than 18.5 or smaller than 10
print("my_house greater than 18.5 or smaller than 10 :", np.logical_or(my_house > 18.5, my_house <10))
# Both my_house and your_house smaller than 11
print("Both my_house and your_house smaller than 11 :", np.logical_and(my_house <11, your_house<11))

# if, elif, else statement
area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")

# Define variables
room = "kit"
area = 14.0
# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed" :
    print("looking around in the bed.")
else :
    print("looking around somewhere.")
# if statement for area
if area > 15 :
    print("big place!")
elif area < 10 : 
    print("very small")
else :
    print("pretty small.")

# filtering pandas
import pandas as pd
cars = pd.read_csv(r'C:\Users\LENOVO\Downloads\cars.csv - Sheet1.csv', index_col=0)
print(cars)

#filtering data drives_right nya yg true
dr = cars['drives_right']
sel = cars[dr]
print(sel)

# the simple way no need to make dr variable
sel = cars[cars['drives_right']]
print(sel)
# mau cari negara yg punya > 500 cars per cap
print(cars[cars['cars_per_cap'] > 500])

# using np.logical 
import numpy as np
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 300)
medium = cars[between]
print(medium)

true_only = medium[cars['drives_right']]
print(true_only)













