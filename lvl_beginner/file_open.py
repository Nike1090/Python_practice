# "r" - Read - Default value.
# Opens a file for reading,error if the file does not exist

# "a" - Append
# Opens a file for appending, creates the file if it does not exist

# "w" - Write
# Opens a file for writing, creates the file if it does not exist

# "x" - Create
# Creates the specified file, returns an error if the file exists

# "t" - Text - Default value
# Text mode

# "b" - Binary
# Binary mode (e.g. images)

FILE = "C:\\Users\\nike9\\OneDrive\\Python practice\\demo.txt"

demo_file = open(FILE, "a")
demo_file.write(input("Enter any info: ") + "\n")
demo_file.close()

demo_file = open(FILE, "r")
print(demo_file.read())
