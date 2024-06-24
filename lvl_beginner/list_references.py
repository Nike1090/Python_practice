
list_a = [1, 2, 3]
print(list_a)

# Passing values by reference
list_b = list_a
# Both lists change
list_b[0] = 5
print(list_a, list_b)
# Copy a list to another
list_c = list(list_a)
# Only the list_c changes
list_c[0] = 10
print(list_a, list_c)