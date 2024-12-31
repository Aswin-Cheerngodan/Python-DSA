#Print 1 to n numbers
def oneToN(n,i=1):
    print(i,end='')
    if i==n:
        return
    oneToN(n,i+1)

# oneToN(9)

#Mean of array
def mean(arr,sm=0,i=0):
    if len(arr)==0:
        return sm/i
    sm+=arr[0]
    i+=1
    return mean(arr[1:],sm,i)

# print(mean([1,2,3]))

def revstr(s):
    if len(s)==0:
        return 
    print(s[-1],end="")
    revstr(s[:-1])

# revstr("qwerty")


