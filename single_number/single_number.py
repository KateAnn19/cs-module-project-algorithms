'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    if len(arr) == 0:
        return "none"
    
    nums = {}
    for i in arr:
        if nums.get(i) is not None:
            nums[i] += 1
        else:
            nums[i] = 1

    for key in nums:
        if nums[key] < 2:
            return key


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")



# understand the problem
    # input
        # a list of integers where every number shows up twice
        # can the numbers be negative?
        # how large can the numbers be?
        # what about 0?
        # are the doubled numbers always beside each other?
        # can the doubled numbers be spread out?
        # can there be triplets of numbers?
    # output
        # a single number 

# plan (pseudocode)
    # looping over numbers
    # comparing numbers to see if they have a double or not
    # what about storing everything in a dictionary and counting each occurrence of the letters?
    #