#There are n kids with candies. You are given an integer array candies,
#where each candies[i] represents the number of candies the ith kid has,
#and an integer extraCandies, denoting the number of extra candies that
#you have.

candies = [2,3,5,1,3]
extraCandies = 3
Output = [True,True,True,False,True]
def kidsWithCandies(candies, extraCandies):
    new = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= max(candies):
            new.append(True)
        else:
            new.append(False)
    return new


#print(kidsWithCandies(candies, extraCandies))


#can also shorten this code by saying:
def kidsWithCandiesShort(candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies ]

print(kidsWithCandiesShort(candies, extraCandies))
