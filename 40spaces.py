# Back in the stone age (before CSS), we used spaces to align
# things on the screen. If we have a 40-character wide table
# of Flintstone family members, how can we center the following
# title above the table with spaces?

title = "Flintstone Family Members"

# padding = (40 - len(title)) // 2
# print(padding)

# print(("." * padding) + title + ("." * padding))

# Above is a confusing approach. Instead, use simple method to simplify:

centered_title = title.center(40)

print(centered_title)
