#url(https://leetcode.com/problems/summary-ranges/description/?envType=problem-list-v2&envId=array)
"""
will start from the beginning of the array and go one step at a time if the element where  our second pointer is not after the previous element
then that  is  a range basically from the first pointer to the (seconde pointer-1) simple 
time complexity: o(n) just looping through the entire array
space complexity: o(1) did not use any extra space 
"""

class Solution(object):
    def summaryRanges(self, nums):
        # we need to handle two cases one element and no elements
        if len(nums) ==0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        list=[]
        s=0
        for r in range (1,len(nums)):
            if nums[r]!=nums[r-1]+1:
                list.append(self.draw_range(nums,s,r-1))
                s=r

        if r==s:
            list.append(self.draw_range(nums,s,r))
        else:
            list.append(self.draw_range(nums,s,r))

        return list

    def draw_range(self,list,l,r):
        if l==r:
            return str(list[l])
        return str(list[l]) + "->" + str(list[r])

print(Solution().summaryRanges([1]))
