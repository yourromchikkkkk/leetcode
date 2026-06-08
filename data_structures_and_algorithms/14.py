class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""

        for idx in range(len(strs[0])):
            for s in strs:
                if idx == len(s) or s[idx] != strs[0][idx]:
                    return res
            res += strs[0][idx]
        
        return res

testCase = ["flower","flow","flight"]
res = Solution().longestCommonPrefix(testCase)
print(res)