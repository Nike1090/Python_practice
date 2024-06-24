def factorial(num: int) -> int:
    if num > 1:
       return num*factorial(num-1)
    else:
       return 1


if __name__ == "__main__":
   print(factorial(0))
   print(factorial(3))