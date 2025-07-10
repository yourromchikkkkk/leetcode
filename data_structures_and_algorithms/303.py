from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx - 1]
        self.nums = nums
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left - 1]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1])
print([-2, 0, 3, -5, 2, -1])
print(f'NUMS {numArray.nums}')
print(numArray.sumRange(0, 2))
print(numArray.sumRange(2, 5))
print(numArray.sumRange(0, 5))