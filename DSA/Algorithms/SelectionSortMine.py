# Selection Sort my implementation
# Time complexity O(N^2)

def selection_sort(arr):

    array_size = len(arr)

    # Determing the positon where the next smallest value will be
    for i in range(array_size-1):
        # assuming that the smallest value is at the current position
        min_index = i
        for j in range(i+1, array_size):
            if (arr[j] < arr[min_index]):
                min_index = j

        # to make sure to grab the minimum value at the index
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)


numbers = list(
    map(int, input("Enter some numbers seperated by commas: ").split(',')))

selection_sort(numbers)
print(f"The sorted list using selection sort is: {numbers}")
