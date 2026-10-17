# Selection Sort Algorithm
# Time Complexity: O(N^2)

# Defining the list/ array
my_array = [10, 65, 1, 25, 6, 5, 14, 3, 2, 0, 8]

# Getting the size/length of the array
n = len(my_array)

# Outer loop will determine where the next smallest
# number should gone, so pretty much the i is incrementing
# up so that once we have the smallest value in the list
# we can throw it into it's correct position then we move to the
# next position and find the next smallest value in the list.
# The n-1 is so that we stop before the array length, since
# we don't want to be sorting past its length
for i in range(n-1):

    # We are making the assumption that
    # the current position holds our minimum value
    min_index = i

    # inner loop is used to search for a smaller number in the
    # unsorted portion of the list.
    # i+1 tells us to start at the position right after our current position
    # n is the stopping boundary
    for j in range(i+1, n):

        # checking if the number at the next position
        # is greater than our number at the minimum index
        # if it is then we set the minimum index to j
        if my_array[j] < my_array[min_index]:

            # Since the value in the position we are checking
            # is smaller than the value at the minimum index
            # when the set the minimum index to j so that
            # the minimum index has the lowest value element
            min_index = j

    # We are now removing the smallest value
    # and setting it equal to min_value
    min_value = my_array.pop(min_index)

    # We are then inserting the miniminum value
    # to the correct position
    my_array.insert(i, min_value)

print(f"Sorted array: {my_array}")
