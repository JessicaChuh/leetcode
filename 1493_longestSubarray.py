#Given a binary array nums, you should delete one element from
# it.

#Return the size of the longest non-empty subarray containing
#only 1's in the resulting array. Return 0 if there is no such
# subarray.

nums = [0,1,1,1,0,1,1,0,1]

def longestSubarray(nums):
    left, right = 0, 0
    zeros = 0
    max_ones = 0

    while right < len(nums):
        if nums[right] == 0:
            zeros += 1

        while zeros > 1:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        max_ones = max(max_ones, right - left)
        right += 1

    if zeros ==  1:
        return max_ones
    elif zeros == 0:
        return max_ones
    else:
        return 0

print(longestSubarray(nums))
