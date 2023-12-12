# indexing
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")
# Use ind_ger to print out capital of Germany
print("Capital city of Germany is " + capitals[ind_ger])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# Print out the keys in europe
print(europe.keys())
# Print out value that belongs to key 'norway'
print("Capital city of Norway is " + europe['norway'])
print("apakah spain bagian dari europe :", 'spain' in europe)
print("apakah madrid bagian dari europe :", 'madrid' in europe)
# adding more variables 
europe['italy']='rome'
europe['poland']='warsaw'
europe['england']='manchester'
europe['indonesia']='jakarta'
print("new more countries : " + str(europe))

# updating dict
europe['england']='london'
# deleting from dict
del(europe['indonesia'])
print("fix countries : " + str(europe))


europe2 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
# mencari data populasi spain
print("populasi negara spain : " + str(europe2['spain']['population']))
# menambahkan data pada dict
data = {'capital' : 'rome','population':59.83}
europe2['italy']=data
print("data baru setelah nambah italy : " + str(europe2))

# using pandas
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap':cpc}
print(my_dict)
print(my_dict.keys())
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)
print(cars)

# mengubah index pada row pandas
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

# importing csv data to pandas
cars = pd.read_csv(r'C:\Users\LENOVO\Downloads\cars.csv - Sheet1.csv', index_col=0)
print(cars)

# customization/filtering
print(cars['country']) # mjd pandas data series
print(cars[['country', 'cars_per_cap']]) # mjd data frame

# filtering berdasarkan urutan
print(cars[0:3])
print(cars[5:7])

# filtering secara spesifik
print(cars.loc[['US', 'JAP']]) # bedanya dgn iloc hanya di penamaan
print(cars.iloc[[0, 2]]) # iloc bikin hemat waktu
print(cars.iloc[[5,6], [0, 2]]) # filtering dgn lebih dari satu variabel
# filtering semua baris pada beberapa kolom
print(cars.iloc[:, [1, 2]])

print(cars.index)
























