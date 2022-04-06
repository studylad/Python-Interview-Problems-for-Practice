# Given an array of numbers, find all the
# pairs of numbers which sum upto `k`


def find_pairs(num_array, k):
    return [(num, (k - num)) for num in num_array if (k - num) in num_array]


result = find_pairs([0, 14, 0, 4, 7, 8, 3, 5, 7], 11)
print(result)
