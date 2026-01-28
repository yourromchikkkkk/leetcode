from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                return min(res, nums[left])
            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return res


testCase1 = [4,5,6,-1,0,1,2]
testCase2 = [4,5,6,7,0,1,2]

solution = Solution()
print(solution.findMin(testCase1))
print(solution.findMin(testCase2))