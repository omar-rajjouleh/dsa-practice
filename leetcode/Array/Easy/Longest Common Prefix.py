#url(https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=array)
#complixty is o(n) where n is the min length of the string in list , space will o(1) did not use any extra space just one var for all cases whther the list had 1000 element or 1 
#solution is just keep adding the char if all the element in the list at that point are the same then added if one of them is not then just return the longest prefix 
#its stright forwrad solution easy 



class Solution(object):
    def longestCommonPrefix(self, strs):
        res=''
        for i in range(len(strs[0])):
            for str in strs:
                if i==len(str) or str[i]!=strs[0][i]:
                    return  res

            res+=strs[0][i]

        return res



solu = Solution()
print(solu.longestCommonPrefix(["abc","a"]))
