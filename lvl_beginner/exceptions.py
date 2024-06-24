def print_box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol must be a string of length 1")

    if width < 2 or height < 2:
        raise Exception("width and height must be greater than or equal to 2")

    print(symbol * width)  # Top line

    # Middle
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)  # Bottom line


if __name__ == '__main__':
    print_box('*', 15, 5)
    try:
        print_box('**', 15, 5)
    except Exception as e:
        print(e)
    try:
        print_box('*', 1, 1)
    except Exception as e:
        print(e)
