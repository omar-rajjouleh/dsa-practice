#url(https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array)
#just forward solution if the last element in the lst is not 9 then increment it by 1 and return the list if its 9 then make it 0 and keep looking if there is 
#another 9 if there are no 9s then just increment the element you are standing on and return the element 
#edge case if all 9s in list then the first element should be [1] followed by zeros just insert it easy 
#time: o(n) space : o(1) we aret iterating across the list no extra space needed

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        if digits[0]==0:
            digits.insert(0,1)
        return digits



print(Solution().plusOne([9,9,9]))



