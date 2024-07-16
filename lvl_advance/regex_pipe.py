import re

def find_names(text):
    names_regex = re.compile(r'Name:(max|Ram|vicky)')

    try: 
        return names_regex.search(text).group()
    except AttributeError:
        return None
    
if __name__ == "__main__":
    find_Max = find_names("Name:Max")
    find_Ram = find_names("Name:Ram")
    find_Vicky = find_names("Name: Vicky")

    print(find_Max)
    print(find_Ram)
    print(find_Vicky)