#url(https://leetcode.com/problems/roman-to-integer/description/?envType=problem-list-v2&envId=string)
class Solution(object):
    def romanToInt(self, s):
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range (len(s)):
            if i==len(s)-1:
                res=res+dic[s[i]]
                break
            if dic[s[i+1]]>dic[s[i]]:
                res-=dic[s[i]]
            else:
                res+=dic[s[i]]
        return res




print(Solution().romanToInt("LVIII"))
