# making loops
# Initialize offset
offset = 8
# Code the while loop
print(" basic while loops :")
while offset != 0 :
    print("correcting...")
    offset = offset -1
    print(offset)

# conditional loops
offset_1 = -6
# Code the while loop
print(" conditional loops : ")
while offset_1 != 0 :
    print("correcting...")
    if offset_1 > 0 :
        offset_1 = offset_1 - 1
    else :
        offset_1 = offset_1 + 1
    print(offset_1)

from operator import index
import numpy as py

import numpy as np
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
np_areas = np.array(areas)

# Code the for loop
print(" for loops :") 
for s in np_areas : # variabel s bisa diganti dgn apa aja 
    print(s)
print(" loops in numpy :")
for index, s in enumerate(np_areas) : # enumerate untuk menghilangkan <built in> fuction index
    print("room " + str(index+1) + ": "+ str(s))
# apabila ingin mengurutkannya dari maka index + 1

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
# Build a for loop from scratch
print(" loops in list :")
for x in house :
    print("the " + x[0] + " is " + str(x[1]) + " sqm")
# atau bisa juga menggunakan cara seperti ini :
print(" cara lain :")
for x, y in house :
    print("the", x, "is", y, "sqm")

# loops in dictionary
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterate over europe
print(" dictionary loops :")
for key, value in europe.items() : # use items so there is no error
    print("the capital of", key, "is", value)

# loops in 2d numpy
baseball_2 = [[180, 78.4],
              [215, 102.7],
              [210, 98.5],
              [188, 75.2]]
np_baseball_2 = np.array(baseball_2)
for w, i in (np_baseball_2) :
    print(w, "lbs", i, "inches")
# mengubah 2d numpy menjadi satu baris - satu baris
print(" numpy menjadi satu baris :")
for a in np.nditer(np_baseball_2) :
    print(a)

# using loops in pandas
import pandas as pd
cars = pd.read_csv(r'C:\Users\LENOVO\Downloads\cars.csv - Sheet1.csv', index_col=0)
print(cars)
# Iterate over rows of cars
print(" loops in pandas :") 
for lab, row in cars.iterrows() :
    print(lab) # lab terdiri dari US, AUS, JAP... dst
    print(row) # row terdiri atas sisanya dibawah IN, RU... dst

# hanya mencari country label dan cars per cap nya dan dr nya
print(" lab mjd baris")
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']) + ": " + str(row['drives_right']))

# lab mjd kolom
for lab, row in cars.iterrows() :
    print(lab, "or", str(row['country']))
    print("brp cpc nya :", row['cars_per_cap'])

# adding new column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row['country'].upper()
print(cars)

# cara lebih gampang
print("cara lebih gampang :")
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)


































