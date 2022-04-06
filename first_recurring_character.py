# Given an input string, find the first
# recurring character in it.


def first_recurring_character(input):
    flag = None
    d = {}
    for char in input:
        if char in d:
            flag = char
            return flag
        d[char] = 1
    return flag


result = first_recurring_character("DFGHJWERGBFGHJ")
print(result)  # G
result = first_recurring_character("ABCDEFGH")
print(result)  # None
result = first_recurring_character("12345642124345")
print(result)  # 4
