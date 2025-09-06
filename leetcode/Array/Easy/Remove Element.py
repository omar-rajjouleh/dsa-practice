"""
url(https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array)
complixty time: o(n) it going to through the whole array if  , for space: o(1) did not use any extra space
just keep traking which is the val and swap it with the element from the back of the array  but make sure the element from the back is not the same val
stright forward solution nothing bad it okay problem 
but there is tricky test case when input is like [1] and val=1 that one was tricky because i chnaged a bit of my code to handle this test case i was returning i+1 and the condition in while was i<j 
which was logical until this test case i changed to i<=j and returnd j+1 for me that was the hard part in the problem  
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==val:
                while j>i and nums[j]==val:
                    j-=1
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
            i+=1

        return j+1
