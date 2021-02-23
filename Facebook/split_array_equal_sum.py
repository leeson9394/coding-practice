# You're given an array made up of positive integers. Split the given array into two smaller arrays where the sums of each smaller array are equal. Print out the two smaller arrays.

# eg.
# [1,2,1,1,3] -> [1,2,1] & [1,3]
# [1,1,1,1,1,5] -> [1,1,1,1,1] & [5]
# [5,2,3] -> [5] & [2,3]

def split_array_equal_sum(arr):
    preSum = 0
    postSum = 0
    for i in range(0, len(arr)):
        preSum += arr[i]
        # print(preSum)
        postSum = 0
        for j in range(i+1, len(arr)):
            postSum += arr[j]
        # print(postSum)
        if preSum == postSum:
            print(i)
            split_point = i + 1
            res = []
            for index in range(split_point):
                res.append(arr[index])
            # print(res, arr[split_point:])    
            return [res, arr[split_point:]]         
    return False                                    # if no equal sum subset can be splited into 

arr1 = [1,2,1,1,3]
arr2 = [1,1,1,1,1,5]
arr3 = [5,2,3]
arr4 = [6,2,3]

result = split_array_equal_sum(arr1)
print(result)