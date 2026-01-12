from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resArray = [1] * len(nums)
    
        prefix, postfix = 1, 1

        for idx in range(len(nums)):
            resArray[idx] = prefix
            prefix *= nums[idx]
        for idx in range(len(nums) - 1, -1, -1):
            resArray[idx] *= postfix
            postfix *= nums[idx]
        return resArray

        

solution = Solution()
testCase = [1,2,3,4]
print(solution.productExceptSelf(testCase))