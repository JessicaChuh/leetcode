#Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.




nums = [0,1,0,3,12]
ans = [1,3,12,0,0]

def removezero(nums):
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)
    return nums
