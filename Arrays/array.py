
# Useful libraries for Data Science

import pandas
import numpy
import statistics
from matplotlib import pyplot as plt


myData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]
print("orignal Data:", myData)
# get length
length = len(myData)


# get the total sum
total = sum(myData)

# get max element
maxNum = max(myData)

# get min element
minNum = min(myData)

# get average
avg = total/length

# get standard deviation
sd = statistics.stdev(myData)

# append


print("\nLength of list:", length)

print("Sum total:", total)
print("Max number:", maxNum)
print("Min number:", minNum)
print("Average:", round(avg, 2))
print("Standard deviation:", round(sd, 2))
