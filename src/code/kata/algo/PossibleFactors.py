__author__ = 'shankar'

#
#Write all the possible numbers which multiply to given number. Eg : 12 can be written as 12*1, 2*6,3*4,2*2*4.
# Dont include 6*2 again or 4*3 as its duplication of 2*6 and 3*4 resp.
import math

def printFactors(prefix, prev, n):
    if n < 2:
        return
    s = int(math.ceil(math.sqrt(n)))
    i = 2
    while i<= s:
        if n % i == 0:
            if i > prev and n/i>= i:
                print "%s%s*%s" % (prefix,i, n/i)
                printFactors('%s%s' % (prefix, i),i, n/i)
        i += 1

if __name__ == "__main__":
    printFactors("", 1, 12)