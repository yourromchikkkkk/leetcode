from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for rowSize in range(len(nums) - 1, 0, -1):
            for idx in range(rowSize):
                nums[idx] = (nums[idx] + nums[idx + 1]) % 10
        return nums[0]

solution = Solution()
testCase = [1,2,3,4,5]
print(solution.triangularSum(testCase))