def print_square(symbol, size):
    ## Top of the square
    print((symbol + " ") * size)
    ## Sides
    print((symbol + (" " * (((size - 2)*len(symbol + " ")) + 1)) + symbol + "\n")* (size - 3) + symbol + (" " * (((size - 2)*len(symbol + " ")) + 1)) + symbol)
    ## Bottom of square
    print((symbol + " ") * size)

symbol = input("Enter a symbol: ")
size = int(input("Enter a size: "))

print_square(symbol, size)
