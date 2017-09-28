#!/bin/python

import os, csv, threading

lock = threading.Lock()

def countcode(input_list):

        tmp = []
        for i in input_list:
            tmp.append(i[1])
        count = {}
        for s in tmp:
            if s in count.keys():
                count[s] += 1
            else:
                count[s] = 1
        #return is list of time + K/V of HttpCode:Count
        #['23/Aug/2010:08:58', {'245': 1, '388': 1, '321': 1, '400': 1}]
        return [input_list[0][0], count]

def parsefile(file):

    parsed_list = []
    with open(os.path.join(path, file), 'r') as currentlog:

        data = currentlog.readlines()
        for line in data:
            time = str(line.split()[3])
            code = line.split()[8]
            parsed_list.append([time[1:18], code])
    return parsed_list
    #[...['23/Aug/2010:08:58', '321'], ['23/Aug/2010:08:58', '388']...]


def parsetime(time_code):

    cut = 0
    tmp = []
    final = []
    for i in range(0, len(time_code)-1):
        if time_code[i+1][0] == time_code[i][0]:
                i+=1
        else:
            for j in range(cut, i+1):
                tmp.append(time_code[j])
            #take a list of the same times to batch count http code
            final.append(countcode(tmp))
            tmp = []
            cut = i+1

    for j in range(cut, len(time_code)):
        tmp.append(time_code[j])
    final.append(countcode(tmp))
    return final


def csv_summary(final_list, lock):
    lock.acquire()
    tmp_final_list = {}
    for i in final_list:
        tmp_final_list[i[0]] = i[1]
    #'23/Aug/2010:08:58': {'245': 1, '388': 1, '321': 1, '400': 1}

    tmp = []     #file exit's data


    #re-open csv as dictionary, previous header items are keys, data inputs are values.
    if os.path.exists('result.csv'):
        with open('result.csv', 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                tmp.append(row)


    #add the remaining data in the final_list
    for preData in tmp:
        hasFound = False
        if  preData['time'] in tmp_final_list:

            for key in preData.keys():
                if key != 'time':
                     if key not in tmp_final_list[preData['time']]:
                        tmp_final_list[preData['time']][key] = 0
                        #find new http status code, add to key under time, value 0

                     tmp_final_list[preData['time']][key] =   int(tmp_final_list[preData['time']][key]) + int(preData[key])

        else:

            tmp_final_list[preData['time']] = {}
            for key in preData.keys():
                if key != 'time':
                    tmp_final_list[preData['time']][key] = int(preData[key])

    header = set()
    for value in tmp_final_list.values():

        for i in value.keys():
            header.add(i)

    header.add('time')
    #header = sorted(list(tmp_final_list.keys()))

    for h in header:
        for key in tmp_final_list.keys():
            if h not in tmp_final_list[key]:
                tmp_final_list[key][h] = 0


    header = sorted(header,reverse=True)


    test_file = open('result.csv','w')
    csvwriter = csv.DictWriter(test_file, delimiter=',', fieldnames=header)


    #print( dict((fn,fn) for fn in header ) )
    csvwriter.writerow(dict((fn,fn) for fn in header))


    for t in sorted(tmp_final_list.keys()):
        tmpChange = {'time':t}
        dictMerged1=dict(tmp_final_list[t].items())
        dictMerged1.update(tmpChange.items())
        csvwriter.writerow(dictMerged1)
    #print (tmp_final_list[t].items())
    #print (tmpChange.items())
    #print (dictMerged1)
    test_file.close()
    lock.release()




#pass logs from /var/log/httpd/ folder to 4 threads
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), './LOG/')

filelist = []
for filename in os.listdir(path):
    if not filename.startswith('.'):
        filelist.append(filename)
fcut = int(len(filelist) / 4)


def run1():
    for file1 in range(0, fcut):            #os.listdir(path):
        k = parsefile(filelist[file1])
        l = parsetime(k)
        csv_summary(l, lock)
        print ('1st Thread')


def run2():
    for file2 in range(fcut, fcut*2):       #os.listdir(path):
        k = parsefile(filelist[file2])
        l = parsetime(k)
        csv_summary(l, lock)
        print ('2nd Thread')

def run3():
    for file3 in range(fcut*2, fcut*3):     #os.listdir(path):
        k = parsefile(filelist[file3])
        l = parsetime(k)
        csv_summary(l, lock)
        print ('3rd Thread')

def run4():
    for file4 in range(fcut*3, fcut*4):     #os.listdir(path):
        k = parsefile(filelist[file4])
        l = parsetime(k)
        csv_summary(l, lock)
        print ('4th Thread')


m1=threading.Thread(target=run1)
m1.start()
m2=threading.Thread(target=run2)
m2.start()
m3=threading.Thread(target=run3)
m3.start()
m4=threading.Thread(target=run4)
m4.start()