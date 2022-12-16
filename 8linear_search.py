# Linear or Sequential Search
def linear_search(A,key):
    index=0
    while index<len(A):
        if A[index]==key:
            return f'result found at index: {index}'
        index+=1
    return -1

L=[84,21,47,96,15]
print(linear_search(L,96))
print(linear_search(L,115))