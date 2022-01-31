#!/usr/bin/env python3

### comprehension lists and dictionaries training v1 ###

### lists

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x for x
list = [x for x in nums]
print("x for x in nums:\n{}".format(list))

# x*x for x in nums
list = [x*x for x in nums]
print("\nx*x for x in nums:\n{}".format(list))

# x for each x in nums if x is even
list = [x for x in nums if x % 2 == 0]
print("\nx for x in nums if x % 2 == 0:\n{}".format(list))

# filter + lambda
list = filter(lambda x: x%2 == 0, nums)
filtered = [x for x in list]
print("\nfilter lambda x % 2 == 0:\n{}".format(filtered))

# (letter, num) pair for each letter in "abcd" and num in "0123"
list = [(letter, num) for letter in 'abcd' for num in range(4)]
print("\n(letter, number) for letter and num:\n{}".format(list))
