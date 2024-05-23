#You are given an integer array nums consisting of n elements, and an integer
#k.

#Find a contiguous subarray whose length is equal to k that has the maximum
# average value and return this value. Any answer with a calculation error
# less than 10-5 will be accepted.

nums = [1,12,-5,-6,50,3]
k = 4

def findMaxAverage(nums,k):
    left = 0
    ans = []
    while left + k <= len(nums):
        ans.append(sum(nums[left:left+k])/k)
        left += 1
    return round(max(ans),5)

print(findMaxAverage(nums,k))
