import re


def find_all_phone_number_regex(text):
    phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    return phone_regex.findall(text)

def find_all_phone_numbers_verbose(text):
    return re.compile(r'''
        \d\d\d
        -
        \d\d\d
        -
        \d\d\d\d''', re.VERBOSE).findall(text)

if __name__ == "__main__":
   text = '''
       If tele phone no: 435-344-5646
       area code: 444-222
       pero dnd si 454-456-4555
    '''

   print(find_all_phone_number_regex(text))
   print(find_all_phone_numbers_verbose(text))