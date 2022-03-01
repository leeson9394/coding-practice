

# Given two parameters (your choice of command line args, STDIN, etc) $count and $file
# print out the $count words that occur the most in $file.
#
# For example I might give you the text of a long news article and want to know the
# 10 most frequently occurring words.
#
# Example call and output:
# $ ./concordance book.txt 10
# the     8230
# and     5067
# of      4139
# to      3651
# a       3017
# in      2659
# it      2082
# his     2008
# i       1972
# that    1950



# The man sprang from his chair and paced up and down the room in
# uncontrollable agitation. Then, with a gesture of desperation, he
# tore the mask from his face and hurled it upon the ground. "You
# are right," he cried; "I am the King. Why should I attempt to
# conceal it?"

import re

def count_words(file, num):
    word_list = []
    with open(file,"r")as f:
        article = f.readlines()
        print(article)
        
        for line in article:
            words = line.split(" ")

            
        counter = 0
        
        res = {}
        for word in words:
            filtered_word = re.sub('[^A-Za-z0-9]+', '', word).lower() # filter all special character and lowercase
            # print(filtered_word)
            if filtered_word in res.keys():
                res[filtered_word] += 1
            else:
                res[filtered_word] = 1
                
        # res = ("and": 5067 ,"the":8320....... )
        
        sorted_result = sorted(res.items(), key = lambda x : -x[1])
        # print(sorted_result)
        for i in range(num):
            print(sorted_result[i][0], sorted_result[i][1])
            
count_words("Facebook/count_words.txt", 10)
    
# Consider a square grid of size grid_size, where grid_size>=3. I have placed a battleship of
# size 3 somewhere in the grid, and you want to sink my battleship by ordering
# the bombing of specified coordinates.
#
# The battleship can only be placed vertically or horizontally, not diagonally.
# Every coordinate which does not contain the battleship is empty. Your task is
# to write a function which takes as input grid_size, and returns the 3 coordinates of
# the battleship.
#
# Assume you have a function, boolean bomb_location(x, y), which will return
# True if (x, y) "hits" the battleship and False if (x, y) misses the 
# battleship.
#
# For example - in the following grid your function find_battleship(grid_size),
# given grid_size of 8,  would return ((2,1), (2,2), (2,3)):
#
# . . . . . . . .
# . . X . . . . .
# . . X . . . . .
# . . X . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .
# . . . . . . . .


# def find_battleship(grid_size, ship_length):
#     row = grid_size
#     col = grid_size
#     for i in range(0,row):
#         for j in range(0,col):
#             if bomb_location(i,j) = True:
#                 result.append([i,j])
            
            
        
    
#     direction = ((-1,0), (1,0), (0,1), (0, -1))
    
    
    
    
#     return result

class Solution:
    def bomb_location(self, i, j):
        target_i = [1,2,3]
        target_j = [2]
        if i in target_i and j in target_j:
            return True
        else:
            return False


    def find_battleship(self, grid_size):
        row = grid_size
        col = grid_size
        visited = False
        ship_coordinates = []
        for i in range(0, row):
            for j in range(0, col):
                bomb_if_hits = self.bomb_location(i,j)
                if bomb_if_hits == True:
                    self.dfs(i, j, grid_size, bomb_if_hits, visited, ship_coordinates)
        return ship_coordinates

    def dfs(self, i, j, grid_size, bomb_if_hits, visited, ship_coordinates):
        if i < 0 or i > grid_size or j < 0 or j > grid_size or bomb_if_hits == False:
            return
        visited = True
        ship_coordinates.append((i,j))
        if visited == False:
            self.dfs(i + 1, j, grid_size, bomb_if_hits, visited, ship_coordinates)
            self.dfs(i - 1, j, grid_size, bomb_if_hits, visited, ship_coordinates)
            self.dfs(i, j + 1, grid_size, bomb_if_hits, visited, ship_coordinates)
            self.dfs(i, j - 1, grid_size, bomb_if_hits, visited, ship_coordinates)

s = Solution()
result = s.find_battleship(8)
print(result)

    

