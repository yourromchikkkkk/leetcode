from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            print('------------')
            print(f"left = {left}; mid = {mid}; right = {right}")
            print(f"left = {nums[left]}; mid = {nums[mid]}; right = {nums[right]}")
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[mid] or target > nums[r]:
                    right = mid - 1
                else:
                     left = mid + 1

    
        return -1
    
solution = Solution()
testCase = [4,5,6,7,8,1,2]
testCase2 = [4,5,6,-1,0,1,2]
testTarget = 1
testTarget2 = 4
# print(solution.search(testCase, testTarget)) # 5
# print(solution.search(testCase2, testTarget)) # 5
print(solution.search(testCase2, testTarget2)) # 0