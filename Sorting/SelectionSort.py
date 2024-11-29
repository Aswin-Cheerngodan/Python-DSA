#Selection sort
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    print(arr)

arr = [45,23,12,34,67,1]
selectionSort(arr)