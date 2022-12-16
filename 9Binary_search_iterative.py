# Binary works only if the list is in sorted order.

def binary_search(A,key):
    Lower=0
    upper=len(A)-1
    while Lower<=upper:
        middle=(Lower+upper)//2
        if A[middle]==key:
            return f"Value found at index: {middle}."
        elif key>A[middle]:
            Lower=middle+1
        elif key<A[middle]:
            upper=middle-1
    return "Not found"

l=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

print(binary_search(l,23))