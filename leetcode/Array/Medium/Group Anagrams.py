#url(https://leetcode.com/problems/group-anagrams/description/)

from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res=defaultdict(list)
        for s in strs:
            #we need to create list of counts where it will count every character in string and it will produce a list
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(s)

        return res.values()


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


