#Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a
# 32-bit integer.

#You must write an algorithm that runs in O(n) time and without
# using the division operation.

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n  # Initialize the answer array with all elements as 1

    # Calculate the product of all elements before nums[i]
    prefix_product = 1
    for i in range(n):
        answer[i] *= prefix_product
        prefix_product *= nums[i]

    # Calculate the product of all elements after nums[i]
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix_product
        suffix_product *= nums[i]
    return answer
