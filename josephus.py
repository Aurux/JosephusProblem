import matplotlib.pyplot as plt

def murderSuicide(array):
    # Work murder (remove) the soldiers to find the "winner".
    while len(array) > 1:

        array.pop(1)
        array.append(array.pop(0))

    return array[0]



n = 10001
totalSoldiers = []
survivorPoints = []

# Check for each value of n.
for i in range(1, n):
    
    array = []
    totalSoldiers.append(i)
    for j in range(i):
        array.append(j+1)
    
    survivor = murderSuicide(array)
    survivorPoints.append(survivor)
    print("For ",i, " soldiers, soldier ",survivor, " will live.")


# Plot data
plt.plot(totalSoldiers,survivorPoints)
plt.title("Josephus problem solutions up to n = "+str(n-1))
plt.xlabel("Total soldiers")
plt.ylabel("Surviving soldier")
plt.show()

