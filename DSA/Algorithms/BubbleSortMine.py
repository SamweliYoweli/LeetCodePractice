def bubble_sort(arr):
    array_size = len(arr)

    for i in range(array_size-1):
        # This can be added so that when the arrays elements
        # are already in order then we can just return the array
        # instead of going through a bunch of passes
        swapped = False

        for j in range(array_size-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break


numbers = list(
    map(int, input("Enter a list of numbers seperated by a comma: ").split(',')))

bubble_sort(numbers)
print(f"Sorted List: {numbers}")
