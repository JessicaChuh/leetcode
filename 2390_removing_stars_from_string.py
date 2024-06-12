#You are given a string s, which contains stars *.

#In one operation, you can:

#Choose a star in s.
# Remove the closest non-star character to its left, as well as
# remove the star itself.
# Return the string after all stars have been removed.

# Note:

# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.

#first try

def RemoveStars(s):
        s = list(s)
        for i in range(s.count('*')):
            if s.index('*') > 0:
                del s[s.index('*')-1:s.index('*')+1]
            else:
                del s[s.index('*')]

        return ''.join(s)

#time complexity is O(n^2), because index() is looping through
# the whole list. where I didn't pass the test where
# len(s) = 10000 and s.count('*') = 5000


#Instead using a stack-based way:

def removeStars(s):
    ans = []
    for i in s:
        if i != '*':
            ans.apend(i)
        elif ans:
            i.pop()

    return ''.join(ans)
