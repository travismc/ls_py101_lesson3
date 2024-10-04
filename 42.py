# Programmatically determine whether 42 lies between 10 and 100,
# inclusive. Do the same for the values 100 and 101.

if 42 in range(10, 101):
    print("42 is between 10 and 100, inclusive.")
else:
    print("42 is NOT between 10 and 100, inclusive.")


if 100 in range(10, 101):
    print("100 is between 10 and 100, inclusive.")
else:
    print("101 is NOT between 10 and 100, inclusive.")


if 101 in range(10, 101):
    print("101 is between 10 and 100, inclusive.")
else:
    print("101 is NOT between 10 and 100, inclusive.")
