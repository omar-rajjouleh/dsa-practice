#url(https://leetcode.com/problems/majority-element/?envType=problem-list-v2&envId=array)
# time is O(n) 
#space is O(N) also used dictionary
# just loop through out the entire array and store every element how much its was occured and then another loop to see if the vale of the key is more than n/2 
#simple ok
# now that for not optimized solution 

"""
now for optimized solution we need to make it o(n) time and o(1) space 
and by that we need to use Boyer–Moore algorithm if we know their is majority element 
the alog goes we pick like element and keep counter that every time we see this element we increment the counter but 
as we going through the array if the element is not the same as the element we pick at first then we decrement the counte 
and if the counter reaches 0 it mean there is another elements that blanced the number  element  in array we pick so we know for sure this element is not the majority element 
and we pick another one as we go and so on 
this alog work actually which is magic to be honest 
"""




class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for num in nums:
            dic.setdefault(num, 0)
            dic[num] += 1

        for key, value in dic.items():
            if value > len(nums) / 2:
                return key

    def majorityElement_optimize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,res=0,0
        for num in nums:
            if count==0:
                res=num
            count+=(1 if num==res else -1)
        return res


print(Solution().majorityElement([2,3,4,2,5]))


