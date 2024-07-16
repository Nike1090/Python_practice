import re

def detect_start_str(phrase):
    return re.compile(r'^Hi').search(phrase)

def detect_end_str(phrase):
    return re.compile(r'World$').search(phrase)

def detect_start_end_str(phrase):
    return re.compile(r'^Hi\sWorld$').search(phrase)

def detect_start_end_digit_str(phrase):
    return re.compile(r'^\d+\s\w+$').search(phrase)

if __name__ == '__main__':
    print(detect_start_str("Vankkam!"))
    print(detect_start_str("Hi"))
    print(detect_end_str("something World"))
    print(detect_start_end_str("Hi World"))
    print(detect_start_end_digit_str("10 Dogs"))