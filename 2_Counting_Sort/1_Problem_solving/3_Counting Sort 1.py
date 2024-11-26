# problem link: https://www.hackerrank.com/challenges/countingsort1/problem

# Solution
def countingSort(arr):
    # print(arr)
    count_arr = [0] * 100
    for i in arr:
        count_arr[i] += 1
    return count_arr