import numpy as np
# Set the seed
np.random.seed(123) # dgn adanya seed hasil yg random akan tetap sama

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
np.random.seed(123)
print(np.random.randint(1, 7))
# Use randint() again
print(np.random.randint(1, 7))
# hasil dua diatas akan tetap sama karean adanya seed

# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)
# Starting step
step = 50
# Roll the dice
dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1, 7)
# Print out dice and step
print("angka dadu yg keluar :", dice)
print("berapa jadinya stepnya :", step)


# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)
# Initialization
random_walk = [0]
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)

# visualize it
import matplotlib.pyplot as plt
plt.plot(random_walk)
plt.show()


# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)


# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)
print(np_aw)
# Plot np_aw and show
plt.plot(np_aw)
plt.show()
# Clear the figure
plt.clf()
# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
print(np_aw_t)
# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand()<= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
print(np_aw_t)
plt.plot(np_aw_t)
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]
# Plot histogram of ends, display plot
plt.hist(ends, edgecolor='white')
plt.show()





























