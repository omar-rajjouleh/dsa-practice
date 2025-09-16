#url(https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=array)
class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i!=j:
                    nums[i] = 0
                j+=1
        return nums

