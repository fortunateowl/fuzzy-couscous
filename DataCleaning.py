#Import Packages

import numpy as np


# Create 2 arrays, arr1 with at least 30 values and outliers, 
# and arr2 with missing values that are str type

arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 
                 50, 60, 70, 80, 690, 100, 10, 20, 30, 40, 50, 760, 70, 
                 80, 90, 1100])

arr2 = np.array([1, 3, 9, 11, 13, 15, 17, 19, " ", 23, 25, 27, 29, 1, 3, 
                 9, 11, 13, 15, "?", 19, 21, 23, 25, 27, 29, 1, 3, 9, 11, 
                 13, 15, 17, "?", 21, 23, 25, 27, 29])


# Function to remove outliers from arr1.
# Takes the argument x that is a numpy array
# Note that the function does not overwrite the varible, but returns an array x
# that can be used to overwrite arr1 or any numpy array of numbers.


def remove_outlier(x):
    
    LimitHi=np.mean(x) + 2*np.std(x)
    LimitLow=np.mean(x) - 2*np.std(x)
        
    x = x[(x < LimitHi) & (x > LimitLow)]
    
    return x


# Function to replace the outliers with the arithmatic mean of the non-outliers.
# Takes the argument y that is a numpy array
# Note that the function does not overwrite the varible, but returns an array y
# that can be used to overwrite arr1 or any numpy array of numbers.


def replace_outlier(y):
    
    LimitHi=np.mean(y) + 2*np.std(y)
    LimitLow=np.mean(y) - 2*np.std(y)
    
    Flag_Good = (y <= LimitHi) & (y >= LimitLow)
    Flag_Bad = ~Flag_Good
    
    y[Flag_Bad] = np.mean(y[Flag_Good])
    
    return y


# Function to replace missing values with the median of the non-outliers.
# The function also converts the array of strings to an array of numbers.
# Takes the argument z that is a numpy array
# Note that the function does not overwrite the varible, but returns an 
# array z that can be used to overwrite arr2 or any numpy array with 
# string, missing values.

    
def fill_median(z):
    
    Flag_Good = np.array([element.isdigit() for element in z])
    Flag_Bad = ~Flag_Good
    
    mdn = z[Flag_Good]
    mdn = mdn.astype(float)
 
    z[Flag_Bad] = np.median(mdn)
    
    z = z.astype(float)
    
    return z




# Demonstrates the function remove_outlier
# 690, 760, and 110 are removed
print ("\n Original array, arr1:")
print (arr1)
print ("\n Outliers removed:")
print (remove_outlier(arr1))

#to overwrite arr1 use the code arr1 = remove_outlier(arr1) 


# Demonstrates the function replace_outlier
# 690, 760, and 1100 are replaced with the arithmatic mean of the 
# non-outliers, 51
print ("\n \n Original array, arr1:")
print (arr1)
print("\n Outliers replaced with mean of non-outliers:")
print (replace_outlier(arr1))

#to overwrite arr1 use the code arr1 = replace_outlier(arr1)
    

# Demonstrates the function fill_median
# string values are replaced with the median (16.0) of the non-missing values   
print ("\n \n Original array, arr2:")
print (arr2)
print("\n Missing values replaced with median of non-missing values:")
print (fill_median(arr2))
    
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

