#url(https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array)

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) ==0:
            return 0
        lst=[]
        lst.append(nums[0])
        for i in range (1,len(nums)):
            if nums[i]!=nums[i-1]:
                lst.append(nums[i])


        nums[:]=lst
        return len(lst)
      
