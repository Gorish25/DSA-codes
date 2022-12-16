# Binary Search using Recursion

def binary_search(A,key,l,u):
    if l>u:
        return "Value Not found"
    else:
        middle=(l+u)//2
        if key==A[middle]:
            return f'Value found at index: {middle}'
        elif key<A[middle]:
            return binary_search(A,key,l,middle-1)
        elif key>A[middle]:
            return binary_search(A,key,middle+1,u)

A=[15,21,47,84,96,103,118,157,189]
print(binary_search(A,118,0,len(A)-1))