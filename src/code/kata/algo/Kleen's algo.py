#
# Given starting and ending positions of segments on a line, the task is to take the union of all given segments and find length covered by these segments.
#
# Examples:
#
# Input : segments[] = {{2, 5}, {4, 8}, {9, 12}}
# Output : 9
# segment 1 = {2, 5}
# segment 2 = {4, 8}
# segment 3 = {9, 12}
# If we take the union of all the line segments,
# we cover distances [2, 8] and [9, 12]. Sum of
# these two distances is 9 (6 + 3)


def findlengthoflinesegments(segments):
    arr = list()
    for (k, v) in segments:
        arr.append((k, False))
        arr.append((v, True))

    k = sorted(arr)
    counter = 0
    result = 0
    i = 0
    while i < len(k):
        if counter > 0:
            result += (k[i][0] - k[i-1][0])
        if k[i][1]:
            counter -= 1
        else:
            counter += 1
        i += 1
    return result


if __name__ == '__main__':
    segments = [(2, 5), (4, 8), (9, 12)]
    print(findlengthoflinesegments(segments))
