#url(https://leetcode.com/problems/range-sum-query-immutable/description/?envType=problem-list-v2&envId=array)
# time complexity is o(1) for query but for declearing  the prefix sum array is o(n) 
#space is o(n) for having additional list 

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # we can have prefixed array here in constructor
        self._prefix= nums
        for i in range (1,len(self._prefix)):
            self._prefix[i] = self._prefix[i] + self._prefix[i - 1]




    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        rightSum=self._prefix[right]
        leftSum=self._prefix[left-1] if left > 0 else 0
        return rightSum - leftSum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj=NumArray([[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]])
print(obj.sumRange(0, 5))
