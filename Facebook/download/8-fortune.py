# import os
# import random
# file = os.popen("wc -l dataset2.csv", 'r').read().split()[0]
# line = random.randint(0, int(file))
# print(line)

import random

def fortune_line(file_path):
    with open(file_path, "r") as f:
        article = f.readlines()
        lucky_line_num = random.randint(0, len(article) - 1)
        print(article[lucky_line_num])
        
file_path = "Facebook/data/hamlet_review.txt"
fortune_line(file_path)