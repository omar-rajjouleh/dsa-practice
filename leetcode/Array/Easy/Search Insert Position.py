#just binary search problem very easy the trick is to return the place where is will be the target if its of bound simple
#url(https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array)
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left if left > right else right


print(Solution().searchInsert([1,3,5,7], 2))
