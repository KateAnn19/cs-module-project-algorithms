'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    zeroArray = []

    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeroArray.append(arr[i])
            print(zeroArray)
        else:
            zeroArray.insert(0,arr[i])
    return zeroArray


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


# understand the problem 
# input is an array of integers
    # integers can be negative
    
# output 
    # where to move zeros?
    # an array with all the zeros in it