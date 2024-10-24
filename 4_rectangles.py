def print_rectangle(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * int(n + 1))
        elif i == int(n/2):
            print("*" * int(n + 1))
        else:
            print("*" + (" " * int(n/2 - 1)) + "*" + (" " * int(n/2 - 1)) + "*")

square_size = int(input("Input a side length: "))

print_rectangle(square_size)
