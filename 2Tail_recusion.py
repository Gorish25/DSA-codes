def calculate_square(n):
    if n>0:
        k=n**2
        print(k)
        calculate_square(n-1)

calculate_square(5)