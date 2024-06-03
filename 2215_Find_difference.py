#Given two 0-indexed integer arrays nums1 and nums2, return a
# list answer of size 2 where:

#answer[0] is a list of all distinct integers in nums1 which
#are not present in nums2.
#answer[1] is a list of all distinct integers in nums2 which
#are not present in nums1.

#Note that the integers in the lists may be returned in any
#order.

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

set1 = set(nums1)
set2 = set(nums2)

diff1 = list(set1 - set2)
diff2 = list[set2 - set1]


print([diff1,diff2])


#TakeAway:
#subtraction operation doesn't work between list but works between
#sets.
