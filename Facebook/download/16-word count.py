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
    word_count = {}
    with open('1.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line.split()
            for word in line:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            line = f.readline()
    heap = []
    for i in word_count:
        heapq.heappush(heap, (-word_count[i], i))
    return heap


if __name__ == '__main__':
    print(dinosaur())

