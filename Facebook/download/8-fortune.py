import os
import random
file = os.popen("wc -l dataset2.csv", 'r').read().split()[0]
line = random.randint(0, int(file))
print(line)
