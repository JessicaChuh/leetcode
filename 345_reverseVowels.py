#Given a string s, reverse only all the vowels in the string and return it.

#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
#lower and upper cases, more than once.



s = "leetcode"
Output = "leotcede"

def reverseVowels(s):
    new = list(s)
    i,j = 0, len(s)-1
    example = ['a', 'e', 'i', 'o', 'u']
    while i < j:
        if new[i].lower() not in example:
            i += 1
            continue
        if new[j].lower() not in example:
            j -= 1
            continue

        new[i],new[j] = new[j],new[i]
        i += 1
        j -= 1

    return "".join(new)

print(reverseVowels(s))
