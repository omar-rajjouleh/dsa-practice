#url(https://leetcode.com/problems/contains-duplicate/submissions/1763445495/?envType=problem-list-v2&envId=array)
#very easy just look if the element presented in the set if it is return true if its not then added to the list 
#time:o(n) searching for element in set is o(1) so its o(n) if we look at all elements in the array
#space: o(n) also we stored every  (element) from the array
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set=set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return True
           

        return False
