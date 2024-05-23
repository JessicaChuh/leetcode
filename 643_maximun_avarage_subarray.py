#You are given an integer array nums consisting of n elements, and an integer
#k.

#Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error
# less than 10-5 will be accepted.

nums = [1,12,-5,-6,50,3]
k = 4

def findMaxAverage(nums,k):
    current_sub = sum(nums[:k])
    max_sub = current_sub

    for i in range(k,len(nums)):
        current_sub = current_sub - nums[i-k] + nums[i]
        max_sub = max(max_sub, current_sub)

    return max_sub/4

print(findMaxAverage(nums,k))
