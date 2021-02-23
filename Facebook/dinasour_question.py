# dinosaurs question

# You will be supplied with two data files in CSV format. The first file contains staticstics about various dinosours. The second file contains additional data.

# Write a program to read in the data files from disk. it must then print the names of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# speed=((STRIDE_LENGTH/LEG_LENGTH)-1)*SQRT(LEG_LENGTH*g)
# Where g = 98m/s^2(gravitational constant)

# dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# TyrannosaurusRex,2.5,carnivore

# dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# TyrannosaurusRex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal

import csv
import math

def print_bipedal_dinosaurs_order_by_speed(file1_path, file2_path):
    with open(file2_path, 'r') as csv2:
        csvReader2 = csv.DictReader(csv2)
        for row in csvReader2:
            if row['STANCE'] == 'bipedal':
                bipedal_dino[row['NAME']] = row['STRIDE_LENGTH']

    with open(file1_path, 'r') as csv1:
        csvReader1 = csv.DictReader(csv1)
        for row in csvReader1:
            if row['NAME'] in bipedal_dino.keys():
                bipedel_dino_leg_length = float(row['LEG_LENGTH'])
                bipedel_dino_stride_length = float(bipedal_dino[row['NAME']])
                speed = ((bipedel_dino_stride_length/bipedel_dino_leg_length)-1)*math.sqrt(bipedel_dino_leg_length*g)
                dino_speed[row['NAME']] = speed
        # print(dino_speed)

        # option 1, sort the dict with lambda function
        res = sorted( dino_speed.items(), key = lambda x: -x[1] )
        for item in res:
            print(item[0])
        # option 2, store dict to tuple pair and sort by value
        # speed_view = [ (v,k) for k,v in dino_speed.items() ]
        # speed_view.sort(reverse=True)
        # for v,k in speed_view:
        #     print(k)

file1_path = "Facebook/dataset1.csv"
file2_path = "Facebook/dataset2.csv"

bipedal_dino = {}
g=9.8
dino_speed = {}
print_bipedal_dinosaurs_order_by_speed(file1_path, file2_path)

# Answer from online
# import math
# import heapq
# def printBipedalDinosaursOrderBySpeed(filePathDinoInfo, filePathAddInfo):
#     bipedalDinosaurs = {}
#     g = 9.8
    
#     with open(filePathAddInfo, 'r') as f:
#         line = f.readline()
#         while line:
#             line = f.readline().strip()
#             if line:
#                 NAME, STRIDE_LENGTH, STANCE = line.split(',')
#                 if STANCE == "bipedal":
#                     bipedalDinosaurs[NAME] = float(STRIDE_LENGTH)
    
#     with open(filePathDinoInfo, 'r') as f:
#         line = f.readline()
#         while line:
#             line = f.readline().strip()
#             if line:
#                 NAME, LEG_LENGTH, DIET = line.split(',')
#                 if NAME in bipedalDinosaurs:
#                     STRIDE_LENGTH, LEG_LENGTH = bipedalDinosaurs[NAME], float(LEG_LENGTH)
#                     bipedalDinosaurs[NAME] = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)
    
#     heap = [(value, key) for key, value in bipedalDinosaurs.items()]
#     fastest = heapq.nlargest(len(heap), heap)  # O(n + mlogn)
#     print(*[name for speed, name in fastest], sep='\n')

# printBipedalDinosaursOrderBySpeed('dataset1.csv', 'dataset2.csv')
            
                