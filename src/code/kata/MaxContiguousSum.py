__author__ = 'shankar'


###
# Dynamic problem:  Given a sequence of n real numbers A(1) ... A(n), determine a contiguous subsequence A(i) ... A(j)
# for which the sum of elements in the subsequence is maximized.
###

def maxContiguousSum(numbers):

    if not numbers:
        return None

    runningCount = numbers[0]
    maxCount = runningCount
    start = 0
    finish = 0
    i = 1
    l = 0
    while i < len(numbers):
        if runningCount > 0:
            runningCount += numbers[i]
        else:
            runningCount = numbers[i]
            l = i

        if runningCount > maxCount:
            maxCount = runningCount
            finish = i
            start = l

        i += 1

    print ("MaxCount: %s, Start: %s, Finish: %s" % (maxCount, start, finish))


if __name__ == "__main__":
    print maxContiguousSum([1,-1, 5, 6, -2, -12, 2, 5, 6, 7, 8, 9])