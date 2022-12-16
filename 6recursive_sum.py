# Sum of N Natural Numbers
def recursive_sum(n):
    if n==0:
        return 0
    return recursive_sum(n-1)+n
    
n=int(input("Enter the number for sum"))
print(recursive_sum(n))