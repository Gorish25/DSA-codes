def calculate_square(n):
    if n>0:
        calculate_square(n-1)
        k=n**2
        print(k)

calculate_square(5)