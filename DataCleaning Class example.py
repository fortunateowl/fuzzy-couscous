#Import Packages

import numpy as np
from DataClean import DataClean as DC


# Create 2 arrays, arr1 with at least 30 values and outliers, 
# and arr2 with missing values that are str type

arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 
                 50, 60, 70, 80, 690, 100, 10, 20, 30, 40, 50, 760, 70, 
                 80, 90, 1100])

arr2 = np.array([1, 3, 9, 11, 13, 15, 17, 19, " ", 23, 25, 27, 29, 1, 3, 
                 9, 11, 13, 15, "?", 19, 21, 23, 25, 27, 29, 1, 3, 9, 11, 
                 13, 15, 17, "?", 21, 23, 25, 27, 29])

    
d = DC()


# Demonstrates the function remove_outlier
# 690, 760, and 110 are removed
print ("\n Original array, arr1:")
print (arr1)
print ("\n Outliers removed:")
print (d.remove_outlier(arr1))

#to overwrite arr1 use the code arr1 = remove_outlier(arr1) 

# Demonstrates the function replace_outlier
# 690, 760, and 1100 are replaced with the arithmatic mean of the 
# non-outliers, 51
print ("\n \n Original array, arr1:")
print (arr1)
print("\n Outliers replaced with mean of non-outliers:")
print (d.replace_outlier(arr1))

#to overwrite arr1 use the code arr1 = replace_outlier(arr1)
   

# Demonstrates the function fill_median
# string values are replaced with the median (16.0) of the non-missing values   
print ("\n \n Original array, arr2:")
print (arr2)
print("\n Missing values replaced with median of non-missing values:")
print (d.fill_median(arr2))
   
#to overwrite arr2 use the code arr2 = fill_median(arr2)




#     Summary Comment Block
#
# The Data Has been cleaned, first by finding and removing outliers, second
# by replacing outliers with the mean, and third by replacing missing values
# with the median.
#
# All three cases will yield data more usable than in its original form. In
# the case of arr1, there were three values considered outliers, 690, 760, and
# 1100. The first time they were removed and the second time they were replaced
# with the arithmatic mean of the non-outliers, 51.  On the other hand, arr2
# containd three missing values that needed to be removed or replaced.  Missing 
# values were replaced with the median of the non-missing values, 16.
# The array also needed to be converted from an array of strings to an array
# of numbers.

