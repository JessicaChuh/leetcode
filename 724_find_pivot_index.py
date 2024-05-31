#Given an array of integers nums, calculate the pivot index of
#this array.

#The pivot index is the index where the sum of all the numbers
#strictly to the left of the index is equal to the sum of all
#the numbers strictly to the index's right.

#If the index is on the left edge of the array, then the left
#sum is 0 because there are no elements to the left. This also
#applies to the right edge of the array.

#Return the leftmost pivot index. If no such index exists,
#return -1.

nums = [-7,1,7,3,6,5,6,-9]

def pivotIndex(nums):
    mid = len(nums)//2 + 1
    while 0 <= mid <= len(nums)-1:
        if sum(nums[:mid]) > sum(nums[mid:]):
            mid -= 1
        elif sum(nums[:mid]) < sum(nums[mid:]):
            mid += 1
        else:
            return mid
    return -1

print(pivotIndex(nums))
