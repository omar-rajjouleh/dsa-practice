#url(https://leetcode.com/problems/majority-element/?envType=problem-list-v2&envId=array)
# time is O(n) 
#space is O(N) also used dictionary
# just loop through out the entire array and store every element how much its was occured and then another loop to see if the vale of the key is more than n/2 
#simple ok


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for num in nums:
            dic.setdefault(num,0)
            dic[num]+=1

        for key,value in dic.items():
            if value>len(nums)/2:
                return key


print(Solution().majorityElement([3,2,3]))
