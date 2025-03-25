DataArray = [2, 3, 2, 1, 3, 5, 7, 9, 3, 5, 2]

def InsertionSort(array):
    i = 1
    for i in range(1, len(array)):
        j = i -1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[i] = array[j]
            j -= 1 
        array[j + 1] = temp
    
    return array

def BinarySearch(arr, target, upper, lower):

    mid = (lower + upper)//2 + 1

    if target == arr[mid]:
        print("target found at index {mid} ")
        return mid
    
    if target > mid:
         BinarySearch(arr, target, upper, mid)
    if target < mid:
         BinarySearch(arr, target, mid, lower)
    humara  point 

    



upper = len(DataArray)
lower = 0

SortedArray = InsertionSort(DataArray)

target  = int(input("What are you looikh for: \n"))

print(BinarySearch(DataArray, target, upper, lower))


