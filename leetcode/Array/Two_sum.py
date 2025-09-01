
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






