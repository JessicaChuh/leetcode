#Given a binary array nums and an integer k, return the maximum
#number of consecutive 1's in the array if you can flip at most
# k 0's.

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

def longestOnes(nums,k):
    left, right = 0,0
    max_zeros = 0
    flips = 0

    while right < len(nums):
        if nums[right] == 0:
            flips += 1

        while flips > k:
            if nums[left] == 0:
                flips -= 1
            left += 1

        max_zeros = max(max_zeros,right-left+1)
        right += 1
    return max_zeros

print(longestOnes(nums,k))
