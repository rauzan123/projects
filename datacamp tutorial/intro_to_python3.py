# membulatkan angka
import pip


print(round(1.678, 1))
print(round(2.678, 2))

# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True
print(type(var1))
# Print out length of var1, len = panjang dari string atau list
print("panjang list var1 : " +str(len(var1)))
# Convert var2 to an integer: out2
out2 = int(var2)
print("hasil angka dari True : "+str(out2))

help(sorted)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]
full = first + second
# Sort full in descending order: full_sorted, if ascending order maka reverse = false
full_sorted = sorted(full, reverse = True)
print("diurutkan dari yang terbesar : " + str(full_sorted))

# length dari string
hari_ini = "minggu ini"
print("panjang kalimat minggu ini : " +str(len(hari_ini)))

# string to experiment with: place
place = "poolhouse"
place_cap = place.capitalize()
place_up = place.upper()
print(place)
print(place_cap)
print(place_up)

# Counting something in string
print("jumlah huruf o : " +str(place.count("o")))
string = "banana 22345"
print("jumlah huruf a : " + str(string.count("a")))
print("jumlah angka 2 : " +str(string.count("2")))

#indexing list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
print("bathroom urutan ke berapa : " + str(areas.index("bathroom")))
print("size bathroom urutan ke berapa : " +str(areas.index(9.50)))

# Create list areas
angka = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
angka.append(24.5)
angka.append(15.45)
print("tambahan angka : " +str(angka))

# Reverse the orders of the elements in areas
angka.reverse()
print("reverse : " + str(angka))

import math
# Definition of radius
r = 0.43

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r**2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500
# Import radians function of math package
from math import radians
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)
print(dist)

import numpy as np
np.array([1,2,3])


x = [15, 10, 2, 84] + [1, 4, 8, 7, 9]
print(x)
y = x.index(x.count(x[8]))
print(y)