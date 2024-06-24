#  Write a program to calculate the percentage of numbers in a given range that contain the digit 7.
def percentage_of_7(given_range: int):
    seven_amount = 0
    numbers = list(range(given_range))
    
    for n in numbers:
        if '7' in str(n):
            seven_amount += 1
    
    return (seven_amount * 100) / len(numbers)


if __name__ == '__main__':
    print(f"{percentage_of_7(11)}%")