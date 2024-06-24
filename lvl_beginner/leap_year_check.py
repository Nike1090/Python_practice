# Write a function isLeapyear() that determines whether a given year is a 
# leap year. A leap year is divisible by 4, but not by 100; also by 400
def isLeapYear(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return "It's a Leap year"
    else:
        return "It's not a Leap year"
    
if __name__ == '__main__':
    print(isLeapYear(2024))  

