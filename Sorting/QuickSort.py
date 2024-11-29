#Quicksort T:O(nlogn)

def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)

        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    

def partition(arr,low,high):
    pivot = arr[high]
    i = low -1

    for j in range(low,high):
        if arr[j]<pivot:
            i += 1
            arr[j],arr[i] = arr[i],arr[j]
    
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1



arr = [56,34,23,12,43]
quickSort(arr,0,len(arr)-1)
print(arr)

