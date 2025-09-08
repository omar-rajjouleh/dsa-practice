#url(https://www.youtube.com/watch?v=Te_MCY4uG-M)
#just say if the value occured before in dict and use abs(i-j) to see if it is less than k yeah simple
#time:o(n) just looking for every element in array if we saw it before and then apply the formula basic stuff
#space:o(n) we used dic to store elements from the array and in worst case we can store almost all the elements in array

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic={}
        for i,value in enumerate(nums):
            if value in dic:
                formula= abs(dic[value]-i)
                if formula <= k:
                    return True
                dic[value]=i
            else:
                dic[value]=i

        return False


