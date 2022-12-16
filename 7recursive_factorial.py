# Factorial using recursion

def rec_fact(n):
    if n == 0:
        return 1
    return rec_fact(n-1)*n

num=int(input("Enter the number: "))
print(rec_fact(num))