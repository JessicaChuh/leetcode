#You are given two strings word1 and word2.
#Merge the strings by adding letters in alternating order, starting with word1.
#If a string is longer than the other, append the additional letters onto the
#end of the merged string.
import itertools

word1 = "abc"
word2 = "pqr"
Output = "apbqcr"

ans = []

def mergeAlternately(word1: str, word2: str):
    for i,j in itertools.zip_longest(word1,word2,fillvalue=""):
        if i: ans.append(i)
        if j: ans.append(j)
    print(''.join(ans))

mergeAlternately(word1, word2)
