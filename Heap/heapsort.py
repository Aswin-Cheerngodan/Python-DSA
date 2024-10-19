# def heapify(arr,n,i):
#     large=i
#     left=2*i+1
#     right=2*i+2
#     if left<n and arr[left]>arr[large]:
#         large=left
#     if right<n and arr[right]>arr[large]:
#         large=right 
#     if large!=i:
#         arr[i],arr[large]=arr[large],arr[i]
#         heapify(arr,n,large)
        
    
# a=[1,23,4,14,5,6,7,9]
# # heapify(a,len(a)//2-1)

# def heapsort(a):
#     for i in range(len(a)//2-1,-1,-1):
#         heapify(a,len(a),i)
#     for i in range(len(a)-1,0,-1):
#         a[i],a[0]=a[0],a[i]
#         heapify(a,i,0)
        
        
        

# heapsort(a)
# print(a)

# def heapify(arr,n,i):
#     large=i
#     left=2*i+1
#     right=2*i+2
#     if left<n and arr[left]>arr[large]:
#         large=left
#     if right<n and arr[right]>arr[large]:
#         large=right
#     if large!=i:
#         arr[i],arr[large]=arr[large],arr[i]
#         heapify(arr,n,large)


# def heapsort(arr):
#     n=len(arr)
#     for i in range(n//2-1,-1,-1):
#         heapify(arr,n,i)
#     for j in range(n-1,0,-1):
#         arr[j],arr[0]=arr[0],arr[j]
#         heapify(arr,j,0)
        
# a=[23,1,123,14,345,567]
# heapsort(a)
# print(a)
        