__author__ = 'shankar'

# Given a range of integers i....j where 1 < i < j - find the number of perfect squares in this range of natural numbers
# Examples of a perfect squares : 25, 36 etc.
# Provide a constant time solution

import math

if __name__ == "__main__":
    print ("Number of perfect squares = %s" % int((math.floor(math.sqrt(21)) - math.ceil(math.sqrt(1))) + 1))
