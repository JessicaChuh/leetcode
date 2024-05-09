#For two strings s and t, we say "t divides s" if and only if
#s = t + t + t + ... + t + t (i.e., t is concatenated with itself
# one or more times).

#Given two strings str1 and str2, return the largest string x
# such that x divides both str1 and str2.

#Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

str1 = "ABABABAB"
str2 = "ABAB"
# Output: "AB"

def gcdOfStrings(str1, str2):
    new1 = str1 + str2
    new2 = str2 + str1

    if new1 == new2:
        shorter = min(str1,str2,key=len)
        left = new1.replace(shorter,"")
        if  left == "":
            return shorter
        else: return left
    return ""

print(gcdOfStrings(str1, str2))

#feeling quite silly for not using math.gcd()
