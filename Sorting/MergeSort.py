#Merge sort Method:1
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)
    
    return merge(sortedLeft,sortedRight)

def merge(left,right):
    result = []
    i=j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

nums = [3, 7, 6, -10, 15,54, 55, -13]
print(mergeSort(nums))

