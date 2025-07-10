from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # {count: index}
        resultDic = {}
        counter = 0
        resultDic[counter] = -1
        maxLength = 0

        for idx in range(len(nums)):
            counter += 1 if nums[idx] == 1 else -1
            if counter not in resultDic:
                resultDic[counter] = idx
            else:
                maxLength = max(maxLength, idx - resultDic[counter])

        return maxLength


solution = Solution()
testCase = [0,1,1,1,1,1,0,0,0]
print(solution.findMaxLength(testCase))

        
        
        