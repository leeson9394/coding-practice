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

def print_bipedal_dinosaurs_order_by_speed(filePathDinoInfo, filePathAddInfo):
    bipedalDinosaurs = {}
    speed = {}
    g=9.8
    with open(filePathAddInfo, "r") as csv_file2:
        csvReader2 = csv.DictReader(csv_file2)
        for rows in csvReader2:
            if rows['STANCE'] == 'bipedal':
                bipedalDinosaurs[rows['NAME']] = rows['STRIDE_LENGTH'] 
    with open(filePathDinoInfo, "r") as csv_file1:
        csvReader1 = csv.DictReader(csv_file1)
        for rows in csvReader1:
            if rows['NAME'] in bipedalDinosaurs.keys(): 
                speed[rows['NAME']] = ((float(bipedalDinosaurs[rows['NAME']])/float(rows['LEG_LENGTH']))-1)*math.sqrt(float(rows['LEG_LENGTH'])*g)

    print({k: v for k, v in sorted(speed.items(), key=lambda item: item[1], reverse=True)})
    
print_bipedal_dinosaurs_order_by_speed("dataset1.csv", "dataset2.csv")

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
            
                