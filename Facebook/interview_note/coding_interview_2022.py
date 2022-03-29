'''
Welcome to Meta!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!
'''

'''
# Given an array of integers greater than zero, find if there is a way to
# split the array in two (without reordering any elements) such that the
# numbers before the split add up to the numbers after the split. If so,
# print the two resulting arrays.
#
# In [1]: can_partition([5, 2, 3])
# Output [1]: ([5], [2, 3])
# Return [1]: True
# 
# In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1])
# Output [2]([2, 3, 2], [1, 1, 1, 2, 1, 1])
# Return [2]: True
# 
# In [3]: can_partition([1, 1, 3])
# Return [3]: False
# 
# In [4]: can_partition([1, 1, 3, 1])
# Return [4]: False
'''

# sum : index
# (5, 0), (7, 1), (10, 2); sum = 10


# [2]

def can_partition(arr):
    if not arr or len(arr) == 1:
        return False
    
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    
    sum_of_arr = 0 
    for i in range(len(arr)):
        sum_of_arr += arr[i]
        if sum_of_arr == sum - arr[i]:
            print(arr[:i], arr[i:])
            return True
        else:
            return False
        
# time o(N)
# space o(1)

arr = [2, 3, 2, 1, 1, 1, 2, 1, 1]
can_partition(arr)


# You will be supplied with two data files in CSV format. The first file
# contains statistics about various dinosaurs. The second file contains
# additional data.
#
# Given the formula:
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
#     where g = 9.8 m/s^2 (acceleration due to gravity on earth)
#
# write a program to read in the data files from disk, it must then print the
# names of only the bipedal (i.e. two-legged) dinosaurs from fastest to slowest. Do not print any
# other information.
#
# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore
#
#
# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

import csv
import math 

# name: xxx, stride: yyy

def print_bipedal(file_path1, file_path2):
    
    bipedal_dino = {}
    dino_speed = {}
    g = 9.8
    with open(file_path2, "r") as f2:
        csv2 = csv.DictReader(f2)
        for row in csv2:
            if row['STANCE'] == "bipedal":
                bipedal_dino[row['NAME']] = row["STRIDE_LENGTH"]
                
    with open(file_path1, "r") as f1:
        csv1 = csv.DictReader(f1)
        for row in csv1:
            if row["NAME"] in bipedal_dino.keys():
                leg_length = row["LEG_LENGTH"]
                stride_length = bipedal_dino[row["STRIDE_LENGTH"]]
                
                # speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
                #     where g = 9.8 m/s^2 (acceleration due to gravity on earth)
                speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)
                dino_speed[row["NAME"]] = speed
                
    
    tup = sorted(dino_speed.items(), key=lambda x: (-x[1], x[0]))
    
    # [(value1, key1), ().....]
    
    for value, key in tup:
        print(key)

        
    # time: o(n + n + n + 1 + 1) = o(N)
    # space: o(n + n + n ) = o(N)






