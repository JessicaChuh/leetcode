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
    mid = 0
    while pointer < len(nums):
        left_sum = sum(nums[:mid])
        right_sum = sum(nums[mid+1:])
        if left_sum > right_sum:
            mid -= 1
        elif left_sum < right_sum:
            mid += 1
        else:
            return mid
    return -1

print(pivotIndex(nums))
