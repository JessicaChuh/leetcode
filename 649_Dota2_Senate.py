#In the world of Dota2, there are two parties: the Radiant and the Dire.

#The Dota2 senate consists of senators coming from two parties. Now the Senate
#wants to decide on a change in the Dota2 game. The voting for this change is a
#round-based procedure. In each round, each senator can exercise one of the two
#rights:

#Ban one senator's right: A senator can make another senator lose all his rights
#in this and all the following rounds.
#Announce the victory: If this senator found the senators who still have rights
#to vote are all from the same party, he can announce the victory and decide on
#the change in the game.

#Given a string senate representing each senator's party belonging. The
#character 'R' and 'D' represent the Radiant party and the Dire party. Then if
#there are n senators, the size of the given string will be n.

#The round-based procedure starts from the first senator to the last senator in
#the given order. This procedure will last until the end of voting. All the
#senators who have lost their rights will be skipped during the procedure.

#Suppose every senator is smart enough and will play the best strategy for his
#own party. Predict which party will finally announce the victory and change the
#Dota2 game. The output should be "Radiant" or "Dire".

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # R = true表示本轮循环结束后，字符串里依然有R。D同理
        R , D = True, True

        # 当flag大于0时，R在D前出现，R可以消灭D。当flag小于0时，D在R前出现，D可以消灭R
        flag = 0

        senate = list(senate)
        while R and D: # 一旦R或者D为false，就结束循环，说明本轮结束后只剩下R或者D了
            R = False
            D = False
            for i in range(len(senate)) :
                if senate[i] == 'R' :
                    if flag < 0: senate[i] = '0' # 消灭R，R此时为false
                    else: R = True # 如果没被消灭，本轮循环结束有R
                    flag += 1
                if senate[i] == 'D':
                    if flag > 0: senate[i] = '0'
                    else: D = True
                    flag -= 1
        # 循环结束之后，R和D只能有一个为true
        return "Radiant" if R else "Dire"

from collections import deque

def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    radiant = deque()
    dire = deque()

    # Initialize the queues with senator indices
    for i, s in enumerate(senate):
        if s == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r, d = radiant.popleft(), dire.popleft()
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"
