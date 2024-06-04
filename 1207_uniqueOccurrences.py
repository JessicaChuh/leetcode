#Given an array of integers arr, return true if the number of
#occurrences of each value in the array is unique or false
#otherwise.

arr = [1,2,2,1,1,3,4]

def uniqueOccurrences(arr):
#     new = set(arr)
#     ans = []
#     for i in new:
#         ans.append(arr.count(i))

#     return True if len(ans) == len(set(ans)) else False

# print(uniqueOccurrences(arr))

#Hash table
    counts = {}
    for i in arr:
        counts[i] = arr.count(i)

    return True if len(counts.values()) == len(set(counts.values())) else False

print(uniqueOccurrences(arr))
