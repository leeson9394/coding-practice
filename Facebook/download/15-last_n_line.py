import os
print(os.popen("tail -2 dataset2.csv", 'r').read())
