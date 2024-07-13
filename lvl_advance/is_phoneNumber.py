import re


def is_phone_number_regex(num):
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    ph = phone_regex.search(num)
    print(ph)
    return ph is not None

if __name__ == "__main__":
   print(is_phone_number_regex('415-345-5656'))