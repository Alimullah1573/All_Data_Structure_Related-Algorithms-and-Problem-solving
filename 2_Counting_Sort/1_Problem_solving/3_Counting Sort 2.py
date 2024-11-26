# Problem link: https://www.hackerrank.com/challenges/countingsort2/problem

# Solution

def countingSort(arr):
    count_arr = [0]*100
    for i in arr:
        count_arr[i] +=1

    for i in range(1,100):
        count_arr[i] += count_arr[i-1]
    return count_arr
