# Insertion sort 
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        curr = arr[i]
        j = i-1
        while j>=0 and curr<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = curr
    print(arr)

insertionSort([45,56,1,34,12,45,56,5])