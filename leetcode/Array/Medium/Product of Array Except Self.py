#url(https://leetcode.com/problems/product-of-array-except-self/)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if we calculated the prefix and then the postfix fix we can find all the products of elements execpt the element
        #itself for example if we have array [1,2,3,4] to find the product of all elements except for 3 we need to find the
        #prefix of the elements before it which is 2 and the postfix fix of all elements after it which is 12 that is it simple baby

        #lest calcuate the prefix and postfix fix for the array
        prefix=[1]*len(nums)
        prefix[0]=nums[0]
        postfix=[1]*len(nums)
        postfix[len(postfix)-1]=nums[-1]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i]
        for i in range (len(nums)-2,-1,-1):
            postfix[i]=postfix[i+1]*nums[i]

        res=[]
        for i in range(len(nums)):
            pre= 1 if i==0 else prefix[i-1]
            post= 1 if i==len(nums)-1 else postfix[i+1]
            res.append(pre*post)

        return res

# time complexity o(n) and space complexity also o(n)


