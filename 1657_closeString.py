word1 = "cabbba"
word2 = "abbccc"
word1_count = {}
word2_count = {}


def closeStrings(word1,word2):
    word1_count = {}
    word2_count = {}
    for i in set(list(word1)):
        word1_count[i] = word1.count(i)
    for j in set(list(word2)):
        word2_count[j] = word2.count(j)

    return True if sorted(word1_count.keys()) == sorted(word2_count.keys()) and sorted(word1_count.values()) == sorted(word2_count.values()) else False

print(closeStrings(word1,word2))
