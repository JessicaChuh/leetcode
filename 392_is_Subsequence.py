#Given two strings s and t, return true if s is a subsequence of t, or false
# otherwise.

#A subsequence of a string is a new string that is formed from the original
#string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (i.e., "ace" is a
# subsequence of "abcde" while "aec" is not).

s = "abc"
t = "ahbgdc"

#First try messed up with the for loop, j should +1 while s[i] != t[j] without
#else condition.
# def isSubsequence(s,t):
#     new = []
#     for i in range(len(s)):
#         for j in range(len(t)):
#             if s[i] == t[j]:
#                 new.append(s[i])
#                 i += 1
#                 j += 1
#             else:
#                 j += 1

#     if s == "".join(new):
#         return True
#     else:
#         return False

def isSubsequence(s,t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        j += 1

    return i == len(s)

print(isSubsequence(s,t))
