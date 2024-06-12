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

def removeStars(self, s: str) -> str:
        s = list(s)
        for i in range(s.count('*')):
            if s.index('*') > 0:
                del s[s.index('*')-1:s.index('*')+1]
            else:
                del s[s.index('*')]

        return ''.join(s)

#time complexity is O(n^2), because index() is looping through
# the whole list of
