
"""
Worst-case: O(N+M).
Average-case: O(N+M).
Best-case: O(N+M).

"""

def count_sort(input_array):
    # Finding the maximum element of input_array.
    M = max(input_array)

    # Initializing count_array with 0
    count_array = [0] * (M + 1)

    # Mapping each element of input_array as an index of count_array
    for num in input_array:
        count_array[num] += 1

    # Calculating prefix sum at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    # Creating output_array from count_array
    output_array = [0] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1

    return output_array

# Driver code
if __name__ == "__main__":
    # Input array
    input_array = [4, 3, 12, 1, 5, 5, 3, 9]

    # Output array
    output_array = count_sort(input_array)

    for num in output_array:
        print(num, end=" ")



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
