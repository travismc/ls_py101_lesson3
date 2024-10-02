

def ending(sentence: str) -> bool:
    if sentence[-1] == "!":
        return True
    else:
        return False


test1 = "This is a question?"
test2 = "This is an exclamation!"

print(ending(test1))
print(ending(test2))
