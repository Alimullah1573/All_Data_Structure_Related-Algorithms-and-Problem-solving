# Problem link : https://www.hackerrank.com/challenges/quicksort3/problem
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])


    print(' '.join(str(x) for x in array))
    return i + 1



def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        

        quickSort(array, low, pi - 1) 
        quickSort(array, pi + 1, high) 
n = int(input())
data = list(map(int,input().split()))
quickSort(data,0,n-1)


