#url(https://leetcode.com/problems/missing-number/description/?envType=problem-list-v2&envId=array)
"""
first method is easy just sort the array then we can find the missing number easily but the thing is it take o(nlogn) time for sorting so not efficient we can do it in o(n)
now for second method which is my favorite because it use formula that i love which is finding the sum of numbers from 1 to n ok now how it work look closely
we know the numbers in array are from 0 to n right so the sum of those numbers are from 1 to n see where iam going 
just find the sum of numbers in array then we do the formula which is (n+1)*n/2 to find the actual sum of number from 1 to n and then subtract the sum of number from array from the actual sum and by that we find the number

but if the sum of numbers in array is equal to sum using formula then we return  0 that is it and by that we decreased  the time complixety from  o(nlogn) to o(n)

"""

class Solution(object):
    def missingNumber(self, nums):
        #we need to find the length of array to define the n
        n=len(nums)
        sum_numbers_formula= ((n+1)*n)//2
        sum_array=0
        for num in nums:
            sum_array+=num

        return sum_numbers_formula-sum_array if sum_numbers_formula>sum_array else 0






