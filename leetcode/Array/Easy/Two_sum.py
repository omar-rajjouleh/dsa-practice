#Two sum problem url(https://leetcode.com/problems/two-sum/)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dic = {}
        for index, value in enumerate(nums):
            nums_dic[value] = index

        for index, value in enumerate(nums):
            if target - value in nums_dic and index != nums_dic[target - value]:
                return [index, nums_dic[target - value]]

        return []

#complexity time=o(n) and space is o(n) we used extra space to decrease the time from o(n^2) bute force approach  to o(n) just by using dictionary 
#the thing is just by looking in the keys of the dictionary it take o(1) it very rare but it can reach o(n) to be honest but it's o(1) in like 99% of use cases so its very rare to be o(n)
#and by that its was solved in o(n) time 


