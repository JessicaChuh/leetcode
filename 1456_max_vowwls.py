#Given a string s and an integer k, return the maximum number
#of vowel letters in any substring of s with length k.

s = "abciidef"
k = 3
vowels = ['a', 'e', 'i', 'o', 'u']

def maxVowels(s,k):
    s = list(s)
    current_v = 0

    for i in range(k):
        if s[i] in vowels:
            current_v += 1

    max_v = current_v


    for j in range(k,len(s)):
        if s[j] in vowels:
            current_v += 1
        if s[j-k] in vowels:
            current_v -= 1
        max_v = max(max_v, current_v)

    return max_v

print(maxVowels(s,k))
