def reverseWords(sentence):
    stack = []
    words = sentence.split()
    for word in words:
        stack.insert(0, word)
    return " ".join(stack)


given_input = "Do or do not, there is no try."
print(reverseWords(given_input))
