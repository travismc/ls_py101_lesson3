# Write two distinct ways of reversing the list without
# mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

sliced_reverse = numbers[::-1]
print(sliced_reverse)


sorted_reverse = sorted(numbers, reverse=True)
print(sorted_reverse)


reversed_func_reverse = list(reversed(numbers))
print(reversed_func_reverse)
