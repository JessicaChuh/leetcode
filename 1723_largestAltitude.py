#There is a biker going on a road trip. The road trip consists
#of n + 1 points at different altitudes. The biker starts his
#trip on point 0 with altitude equal 0.

#You are given an integer array gain of length n where gain[i]
#is the net gain in altitude between points i​​​​​​ and i + 1 for
#all (0 <= i < n). Return the highest altitude of a point.

gain = [-5,1,5,0,-7]

def largestAltitude(gain):
    altitudes = []
    start = 0

    for i in gain:
        altitudes.append(start+i)
        start += i

    return max(altitudes) if max(altitudes)>0 else 0

print(largestAltitude(gain))
