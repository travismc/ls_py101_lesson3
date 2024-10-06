# Example A
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Anticipated output will be: ['one'] ['two'] ['three'];
# the mess_with_vars function changes values in local scope
# but does not return anything, so no global variable reassignment.


# Example B

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Again, anticipated output will be: ['one'] ['two'] ['three'];
# the mess_with_vars function changes values in local scope
# but does not return anything, so no global variable reassignment.


# Example C

def mess_with_vars(one, two, three):
    one[0] = "two"  # list passed by reference
    two[0] = "three"  # list passed by reference
    three[0] = "one"  # list passed by reference


one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

# Again, anticipated output will be: ['one'] ['two'] ['three'];
# the mess_with_vars function changes values in local scope
# but does not return anything, so no global variable reassignment.
# HOWEVER- the mess_with_vars function modifies the content of the
# lists directly. Since lists in Python are mutable and passed by
# reference, the changes are reflected outside the function.
