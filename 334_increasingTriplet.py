#Given an integer array nums, return true if there exists a triple of indices
#(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
#indices exists, return false.


nums = [2,1,5,0,4,6]
Output = True

#
# def increasingTriplet(nums):
#     conbine = len(nums) -2
#     for i in range(conbine):
#         if nums[i] < nums[i+1] < nums[i+2]:
#             return True
#         else:
#             continue
#     return False

#问题理解有误，这三个integer 不需要相连


#def increasingTriplet(nums):
    # min_index = nums.index(min(nums))
    # max_index = nums.index(max(nums))

    # if min_index >= max_index:
    #     return False
    # else:
    #     for i in range(min_index,max_index):
    #         if min(nums)  < nums[i] < max(nums):
    #             return True
    #         else:
    #             continue
    #         return False


def increasingTriplet(nums):
    if len(nums) < 3:
        return False

    smallest, second_smallest = float('inf'),float('inf')
    for num in nums:
        if num <= smallest:
            smallest = num
        elif num <= second_smallest:
            second_smallest = num
        else:
            return True
    return False

print(increasingTriplet(nums))
