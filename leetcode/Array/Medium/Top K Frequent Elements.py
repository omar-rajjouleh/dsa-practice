from enum import nonmember
#url(https://leetcode.com/problems/top-k-frequent-elements/description/)

class Solution(object):
    def topKFrequent(self, nums, k):
            #dictionary to count how many element occurred
        counts = {}
        #frequnecy array to correspond for every element and how many time it was counted
        #like if element (1) and (2) occurred 3 times in array they will be the values of the index 3 in freq array
        freq=[[] for i in range(len(nums)+1)]
        for number in nums:
            counts[number] = counts.get(number, 0) + 1

        for n,c in counts.items():
            freq[c].append(n)


        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res



#time complexity is o(n) and space complexity is o(n)

print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))
