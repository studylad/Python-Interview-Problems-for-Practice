def permutations(word):
    if len(word) == 1:
        return [word]
    result = []
    for p in permutations(word[1:]):
        print(p, word[1:])
        print("\n")
        for i in range(len(word)):
            print(i, f"1{p[:i]}", "2" + word[:1], f"3{p[i:]}")
            result.append(p[:i] + word[:1] + p[i:])

    return result


given_input = "bc"
print(permutations(given_input))
