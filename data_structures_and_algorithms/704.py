from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        left, right = 0, len(nums) - 1

        while left <= right:
            midIdx = (left + right) // 2
            print(f"left = {left}; right = {right}; midIdx = {midIdx}")
            if nums[midIdx] == target:
                return midIdx
            elif nums[midIdx] > target:
                right = midIdx - 1
            elif nums[midIdx] < target:
                left = midIdx + 1

        return -1


solution = Solution()
testCase1 = [5]
testTarget1 = 5
print(solution.search(testCase1, testTarget1))