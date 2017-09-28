# Given an array of integers, print out the longest sequence of positive integers.  For example, given {-1, 2, 3, -4, 6, 12, 8, 9, -3, -5}, print out {6, 12, 8, 9}

# def positive_array(arr):
#     pos=[]
#     result=[]
#     max_length = 0
#     for i in xrange(len(arr)):
#         if arr[i] > 0:
#             pos.append(arr[i])
#         # else:
#         if arr[i] < 0 or i == (len(arr) - 1):
#             result.append(pos)
#             pos = []
#     print result
#     for i in xrange(len(result)):
#         if max_length < len(result[i]):
#              max_length = len(result[i])
#              max=i
#     return result[max]


def positive_array(arr):
    pos=[]
    res=[]
    max_length = 0
    for index in xrange(len(arr)):
        if arr[index] > 0:
            pos.append(arr[index])
        if arr[index] <= 0 or index == len(arr) - 1: # append if last item positive
            res.append(pos)
            pos=[]
    print res


    for index in xrange(len(res)-1):
        if max_length < len(res[index]):
            max_length = len(res[index])
            max_index = index
    return res[max_index]

# list=[-1, 2, 3, -4, 6, 12, 8, 9, -3, -5, 0, -3, 7 ]
list=[-1, 2, 3, -4, 6, 12, 8, -9, -3, 5, 0, 3, 7 ]
print positive_array(list)