# Problem link: https://www.hackerrank.com/challenges/countingsort2/problem

# Solution

def countingSort(arr):
    res = []
    for i in range(max(arr) + 1):
        res += arr.count(i) * [i]
    return res
