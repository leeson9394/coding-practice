# Leetocde #442 Find All Duplicates in an Array

def findDuplicates(arr):
    # left = 0
    # right = len(arr) - 1
    # arr.sort() 
    # res = []
    # for i in range(len(arr)-1):
    #     if arr[i] == arr[i+1]:
    #         res.append(arr[i])
    # return res
    kv = {}
    res = []
    for i in range(len(arr)):
        if arr[i] in kv:
            res.append(arr[i])
        kv[arr[i]] = i
    return res

array = [4,3,2,7,8,2,3,1]
result = findDuplicates(array)
print(result)