#You have a long flowerbed in which some of the plots are planted,
#and some are not. However, flowers cannot be planted in adjacent plots.

#Given an integer array flowerbed containing 0's and 1's, where 0 means
#empty and 1 means not empty, and an integer n, return true if n new
#flowers can be planted in the flowerbed without violating the
#no-adjacent-flowers rule and false otherwise.

flowerbed = [0,1,0,0,0,0,0,1,0,0,0,1,0]
n = 3
Output: True

def canPlaceFlowers(flowerbed, n):
    if flowerbed.count(0)//3 > n:
        return True
    else:
        return False

print(canPlaceFlowers(flowerbed, n))
