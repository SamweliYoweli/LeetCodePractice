# Bubble Sort
# main idea of bubble sort is checking adjacent
# elements and swapping in the one to the left is
# greater than the one to the right
# Time Complexity of O(N^2)

# creating the array
my_array = [10, 65, 1, 25, 6, 5, 14, 3, 2, 0, 8]

# getting the length of the array
n = len(my_array)

# Our outer loop is what controls how many passes
# we make with the bubble sort so in this case we make 10 passes
for i in range(n-1):
    # This loop controls the neighbors elements getting compared during
    # each pass. we already know that n is our total number of elements
    #  while i is the number of passes already completed
    # -1 prevents us from going beyond of limit of n elements
    # For example, in our first pass the biggest element will already
    # be sorted so there is no need for us to compare or sort it anymore
    for j in range(n-i-1):
        # We are comparing the current element,
        # and checking if it's bigger then the element to the right
        # we are only comparing adjacent numbers
        if my_array[j] > my_array[j+1]:
            # If that's the case then we swap the position of our elements
            # I added the temp variable to hold the value of the array
            # in the current position j so that it doesn't get overwritten
            temp = my_array[j]
            my_array[j] = my_array[j+1]
            my_array[j+1] = temp

print(f"Sorted array: {my_array}")
