#You are given an integer array nums and an integer k.

#In one operation, you can pick two numbers from the array whose sum equals
# k and remove them from the array.

#Return the maximum number of operations you can perform on the array.


nums = [1,2,3,4]
k = 5
Output = 2

def maxOperations(nums,k):
    nums.sort()
    left = 0
    right = len(nums)-1
    max_number = 0

    while left < right:
        if nums[left] + nums[right] == k:
            max_number += 1
            left += 1
            right -= 1
        elif nums[left] + nums[right] < k:
            left += 1
        else:
            right -= 1
    return max_number
