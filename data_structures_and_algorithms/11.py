from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0

        left, right = 0, len(height) - 1

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            maxWater = max(maxWater, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater



solution = Solution()
# testCase = [1,8,6,2,5,4,8,3,7]
testCase = [1, 1]
# testCase = [4,3,2,1,4]
print(solution.maxArea(testCase))
