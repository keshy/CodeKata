__author__ = 'shankar'


# take an array and print non over lapping in order pairs. example:


# [1,2,3,4] => input

# output below is in order combination

# (1234)
# (1)(234)
# (1)(23)(4)
# (1)(2)(34)
# (12)(34)
# (12)(3)(4)
# (123)(4)
# (1)(2)(3)(4)

# 1,2,3
# 1 (2,3)
# (12) 3
# 1 2 3
#
# 12
# 1 2


def PrintCombo(arr, start, str):
    if not arr:
        return None

    if (start == len(arr)):
        print(str)
        return

    for i in xrange(start, len(arr)):
        PrintCombo(arr, i+1, str + '(' + ''.join(arr[start:i+1]) + ')')

    return




if __name__ == "__main__":
    PrintCombo(['1', '2', '3', '4'], 0, '')
