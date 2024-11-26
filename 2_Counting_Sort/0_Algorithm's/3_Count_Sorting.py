
"""
Worst-case: O(N+M).
Average-case: O(N+M).
Best-case: O(N+M).

"""


def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    # Create a count array of size (max_val + 1) and initialize to 0
    count = [0] * (max_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)  # Add the number `i`, `freq` times

    return sorted_arr


# Example usage
a = [3, 1, 0, 2, 1, 4]
sorted_a = counting_sort(a)
print(sorted_a)




# Second sestem
def counting_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    # Create a count array of size (max_val + 1) and initialize to 0
    count = [0] * (max_val + 1)

    # Count the occurrences of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)  # Add the number `i`, `freq` times

    return sorted_arr


# Example usage
a = [3, 1, 0, 2, 1, 4]
sorted_a = counting_sort(a)
print(sorted_a)
