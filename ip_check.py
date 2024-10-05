# Original function:

# def is_dot_separated_ip_address(input_string):
#     dot_separated_words = input_string.split(".")
#     while len(dot_separated_words) > 0:
#         word = dot_separated_words.pop()
#         if not is_an_ip_number(word):
#             break

#     return True


# This initial solution works, except when presented with
# letters that cannot cast to int.

# def is_dot_separated_ip_address(input_string: str) -> bool:
#     is_an_ip_number = list(range(0, 256))
#     # print(is_an_ip_number)
#     dot_separated_words = input_string.split(".")
#     if len(dot_separated_words) != 4:
#         return False

#     while (dot_separated_words):
#         word = dot_separated_words.pop()
#         if int(word) not in is_an_ip_number:
#             return False

#     return True


# This solution works across all edge cases presented.

def is_an_ip_number(str: str) -> bool:
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False


def is_dot_separated_ip_address(input_string: str) -> bool:
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True


print(is_dot_separated_ip_address("255.255.255.255"))
print(is_dot_separated_ip_address("0.0.0.0"))
print(is_dot_separated_ip_address("2.2.111.245"))
print(is_dot_separated_ip_address("2.2.111.6f"))
print(is_dot_separated_ip_address("1.-2.1.1"))
print(is_dot_separated_ip_address("1.256.3.3"))
print(is_dot_separated_ip_address("1.1.300.2"))
print(is_dot_separated_ip_address("1.1.2"))
print(is_dot_separated_ip_address("1.1.30.2.5"))


# Alyssa reviewed Ben's code and said, "It's a good start,
# but you missed a few things. You're not returning a false
# condition, and you're not handling the case when the input
# string has more or less than 4 components, e.g., 4.5.5 or
# 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code.
