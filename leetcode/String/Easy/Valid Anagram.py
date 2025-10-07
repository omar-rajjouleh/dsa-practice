#url(https://leetcode.com/problems/valid-anagram/description/)
#time complexity is O(n) where n is the len(s+t)
#space complexity is O(n) 
#just store every char of s and t in dictionary then compare them like if every key exsists in two dictionaries and they have the same value then the are Anagram and return true 
#else we return false they are not Anagram that is it simple 
class Solution(object):
    def isAnagram(self, s, t):
      if len(s) != len(t):
          return False
      s_dict={}
      t_dict={}
      for i in range(len(s)):
          s_dict[s[i]] = s_dict.get(s[i], 0) + 1
          t_dict[t[i]] = t_dict.get(t[i], 0) + 1

      for char in s_dict:
          if s_dict[char] != t_dict.get(char, 0):
              return False
      return True

