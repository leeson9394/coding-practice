# def insertion_sort(arr):
#     for i in range(1, len(arr)): # unsorted element i as target, start from second value
#         j = i - 1 # reset j
#         current = arr[i] # store target value since array elements will move backwards later
#         while j >= 0 and current < arr[j]: # if unsorted element smaller
#             arr[j+1] = arr[j] # move all element backward one space
#             j = j - 1 # move compare cursor j to front
#         arr[j+1] = current # insert the value to the position after no more value smaller than current
#     return arr

# arr = [15,41,13,2,91]
# print(insertion_sort(arr))


def insertion_sort(arr):
    for j in range(1, len(arr)):
        i = j - 1 # reset cursor i
        cur = arr[j] # store target value since array elements will move backwards later
        while i >= 0 and cur < arr[i]: # if unsorted element smaller
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = cur
    return arr

arr = [15,41,13,2,91]
print(insertion_sort(arr))