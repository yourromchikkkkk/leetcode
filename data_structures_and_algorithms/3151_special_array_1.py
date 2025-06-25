from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        for idx in range(len(nums) - 1):
            if nums[idx] % 2 == nums[idx + 1] % 2:
                return False
        
        return True

solution = Solution()
testCase = [1,5]
print(solution.isArraySpecial(testCase))