"""
A string is modified to add spaces and justification.
"""
# Left and right justification
print("Hola".ljust(10))
print("Hola".rjust(10))
# Center justification, title style
print("Titulo".center(20, "-"))
print("Titulo".center(20, "="))
# Version without center
lines = "-" * 7
print(lines + "Titulo" + lines)