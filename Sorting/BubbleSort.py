#Bubble sort T:O(n2) S:O(1)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
    


arr = [12,1,34,3,6,9,3,2,4]
bubbleSort(arr)



# Improved Bubble
def bubbleSortIm(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        #Breaks when no swapping occurs
        if not swapped:
            break
    print(arr)

arrr = [12,1,34,3,6,9,3,2,4,0,122]
bubbleSortIm(arrr)


