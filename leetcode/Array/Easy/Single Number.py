#just use xor operator to cancel the dupplicated elements
#for example 2^2 =0
"""
url (https://leetcode.com/problems/single-number/?envType=problem-list-v2&envId=array)

"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0 # n^0 = n
        for num in nums:
            res^=num

        return res

