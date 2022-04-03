import csv
import numpy as np
import heapq
g = 9.8


def readFromCSV(file_name):
    d = {}
    with open(file_name, 'r') as f:
        f.readline()
        f_csv = csv.reader(f)
        for item in f_csv:
            if file_name == 'dataset2.csv' and item[2] != 'bipedal':
                continue
            d[item[0]] = float(item[1])
    return d


def dinosaur():
    name_stride = readFromCSV('dataset2.csv')
    name_leg = readFromCSV('dataset1.csv')
    heap = []
    for name in name_leg:
        if name not in name_stride:
            continue
        stride = name_stride[name]
        leg = name_leg[name]
        speed = ((stride / leg) - 1) * np.sqrt(leg * g)
        heapq.heappush(heap, (speed, name))
    return [i[1] for i in heap], heap


if __name__ == '__main__':
    print(dinosaur())

