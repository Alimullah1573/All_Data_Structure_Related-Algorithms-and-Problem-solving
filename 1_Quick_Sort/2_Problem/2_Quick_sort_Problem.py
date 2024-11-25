

# Problem link : https://www.hackerrank.com/challenges/quicksort1/copy-from/411309411


def quickSort(arr):
    p = arr[0]
    left, equal, right = list(), [p], list()
    for a in arr[1:]:
        if a < p:
            left.append(a)
        if a > p:
            right.append(a)
    return left + equal + right