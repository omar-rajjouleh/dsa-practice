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
      for char in s:
          s_dict[char]=s_dict.get(char,0)+1
      for char in t:
          t_dict[char]=t_dict.get(char,0)+1

      for key in s_dict:
          if key in t_dict:
              if s_dict[key] != t_dict[key]:
                  return False
          else:
              return False

      return True
