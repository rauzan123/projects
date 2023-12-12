# topic about lists

fam = ["kenyek", 145, "sasa", 160, "ozan", 170, "mom", 150, "dad", 165]
print(fam)
print(type(fam))

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50
# Create list areas
areas = [hall,kit,liv,bed,bath, 180, "stranger"]
# Print areas
print(areas)

angka = [[1, 2, 3], [4, 5, 7]]
random = [1 + 2, "a" * 5, 3]
print(angka)
print(random)

print(fam[3])
fam2 = ['kenyek', 123, 'sasa', 161, 'ozan', 170, 'dad', 145]
print(fam2[3])
print(fam2[6])
print(fam2[-1])
# so, untuk mengurutkan list, misal fam2[3], maka pengurutan dimulai setelah urutan ke 3, 
# contohnya seperti diatas

print(fam2[3:5])
# jadi, maksud dari 3:5 adalah start after urutan ke 3 end sebelum urutan 5
print(fam2[1:4])
print(fam2[:4])
print(fam2[4:])

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]
# Print the variable eat_sleep_area
print(eat_sleep_area)

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Use slicing to create downstairs
downstairs = areas[0:6]
# Use slicing to create upstairs
upstairs = areas[6:10]
# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# Alternative slicing to create downstairs
downstairs = areas[:6]
# Alternative slicing to create upstairs
upstairs = areas[6:]
print(downstairs)
print(upstairs)
print(type(areas))

# memanipulasi data dalam sebuah lists 
print(areas)
areas[1] = 10.5
areas[4] = "chill zone"
print(areas)

# menambahkan data pada suatu lists dengan membentuk variabel baru/ lists yang baru
areas_1 = areas + ["poolhouse", 20.45]
areas_2 = areas_1 + ["garage", 15.45]
print(areas_2)

# deleting data pada lists
del(areas_2[-4:-2])
print(areas_2)

# cara mengganti data pada sebuah lists tetapi tidak berefek pada data yang satunya
# Create list areas
int_areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = int_areas
areas_copy = int_areas[:]
areas_copy[0] = 5.0

print(int_areas)

#atau bisa juga dengan cara list()
areas_copy_2 = int_areas
areas_copy_2 = list(int_areas)
areas_copy_2[0:4] = 10.0, 11.1, 12.2, 13.3, 14.4
print(areas_copy_2)
print(int_areas)
