def partition(arr, left, right):
    i = (left-1)         # index of smaller element
    pivot = arr[right]     # pivot
 
    for j in range(left, right):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# left  --> Starting index,
# right  --> Ending index
 
# Function to do Quick sort
 
 
def quick_sort(arr, left, right):
    if len(arr) == 1:
        return arr
    if left < right:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, left, right)
 
        # Separately sort elements before
        # partition and after partition
        quick_sort(arr, left, pi-1)
        quick_sort(arr, pi+1, right)
    return arr


arr = [15,41,13,2,91]
print(quick_sort(arr, 0, len(arr) - 1))