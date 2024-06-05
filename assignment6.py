import matplotlib.pyplot as plt
import random
import fileinput
import numpy as np
file_name = "checking_40_cities.txt"
def city_extraction():                                      #to extract the tuples from given text file
    list1, x_cities, y_cities, initial = [], [], [], []

    for line in fileinput.input(files=file_name):
        line = line.split()
        list1.append(line)
    for i in range(1, len(list1)):
        x_cities.append(float(list1[i][0]))
        y_cities.append(float(list1[i][1]))

        initial.append(int(i - 1))
    np.random.shuffle(initial)                          #giving initial order

    return initial, x_cities, y_cities

def main():

    #the following code is similar to the city_extraction function

    list1, x_cities, y_cities, initial = [], [], [], []

    for line in fileinput.input(files =file_name):
        line = line.split()
        list1.append(line)
    n = int(list1[0][0])
    for i in range(1, len(list1)):
        x_cities.append(float(list1[i][0]))
        y_cities.append(float(list1[i][1]))
        initial.append(int(i-1))
    np.random.shuffle(initial)

    x_cities = np.array(x_cities)
    y_cities = np.array(y_cities)
    temp_order = (initial)

    T = 10000
    iterations = 10000
    for i in range(iterations):
        T = 0.99 * T
        optimum = temp_order.copy()
        swap_random(temp_order)
        dist_change = distance(x_cities, y_cities, temp_order) - distance(x_cities, y_cities, optimum)
        if dist_change < 0:
            pass
        else:
            prob = np.exp(-dist_change / T)
            rand = np.random.random_sample()
            if prob > rand:
                pass
            else:
                temp_order = optimum.copy()
    return temp_order

def swap_random(seq):                   #function made to swap any two of the indices randomly
    idx = range(len(seq))
    i1, i2 = random.sample(idx, 2)
    seq[i1], seq[i2] = seq[i2], seq[i1]
    return seq

def distance(x_cities, y_cities, finalorder):       #function to calculate distance of the entire loop
    dist = 0
    for i in range(len(finalorder)):
        dist += pow((x_cities[finalorder[-i]] - x_cities[finalorder[-i-1]])**2 + ((y_cities[finalorder[-i]] - y_cities[finalorder[-i-1]])**2), 0.5)
    return dist

initial, x_cities, y_cities = city_extraction()
optimum = main()
print(f"Minimum path distance is: {distance(x_cities, y_cities, optimum)} using the following order: {optimum}")
print(f"Initial path distance was:{distance(x_cities, y_cities, initial)} with the order: {initial}")
print(f"Percentage improvement: {100*(distance(x_cities, y_cities, initial) - distance(x_cities, y_cities, optimum))/distance(x_cities, y_cities, initial)}%")

#plotting the final optimum path
x_cities = np.array(x_cities)
y_cities = np.array(y_cities)

xplot = x_cities[optimum]
yplot = y_cities[optimum]
xplot = np.append(xplot, xplot[0])
yplot = np.append(yplot, yplot[0])
plt.plot(xplot, yplot, 'o-')
plt.savefig("image_final.png")