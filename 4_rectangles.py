def print_square1(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        elif i == int(n/2):
            print("*" * n)
        else:
            print("*" + (" " * int(n/2 - 1)) + "*" + (" " * int(n/2 - 1)) + "*")

square_size = int(input("Input a side length"))

print_square1(square_size)
