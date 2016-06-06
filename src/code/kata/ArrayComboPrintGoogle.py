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

def PrintCombo(arr, n=0):
    if not arr:
        return None

    if len(arr) == n:
        return arr

    for i in xrange(n, len(arr)):
        print("(" + ''.join(arr[0:n]) + ')' + '(' + ''.join(arr[n:i + 1]) + ')' + '(' + ''.join(arr[i + 1:]) + ')')

    return PrintCombo(arr, n=n + 1)


if __name__ == "__main__":
    PrintCombo(['1', '2', '3', '4'])
