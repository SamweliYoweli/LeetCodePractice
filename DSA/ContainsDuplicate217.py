nums = [1, 2, 3, 1]


# This implementation has a time complexity of O(N^2)
# this was my first crack at it
def contain_duplicate():
    array_size = len(nums)
    for i in range(array_size):
        for j in range(i+1, array_size):
            if (nums[i] == nums[j]):
                return True
    return False

# This implementation has a time complexity of O(N)
# This one uses sets which means duplicates are not allowed
# and They are unordered and unchangeable

def improved_contain_duplicate():
    if (len(set(nums)) == len(nums)):
        return False
    else:
        return True
