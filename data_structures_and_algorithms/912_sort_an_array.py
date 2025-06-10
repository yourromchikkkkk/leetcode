class Solution(object):
    def swap(self, nums, idx1, idx2):
        temp = nums[idx1]
        nums[idx1] = nums[idx2]
        nums[idx2] = temp
    
    def partition(self, nums, low, high):
        pivot = nums[high]
        idx = low - 1
        for j in range(low, high):
            if (nums[j] <= pivot):
                idx += 1
                self.swap(nums, idx, j)
        self.swap(nums, idx + 1, high)
        return idx + 1
    
    def quickSort(self, nums, low, high):
        if (low < high):
            partitionIdx = self.partition(nums, low, high)

            self.quickSort(nums, low, partitionIdx - 1)
            self.quickSort(nums, partitionIdx + 1, high)
    
    def quickSortV2(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quickSortV2(left) + middle + self.quickSortV2(right)
    
    def findSmallest(self, nums):
        idx = 0
        for index in range(1, len(nums)):
            if (nums[index] < nums[idx]):
                idx = index
        return idx
    
    def selectionSort(self, nums):
        newArr = []
        for _ in range(len(nums)):
            smallestIndex = self.findSmallest(nums)
            newArr.append(nums.pop(smallestIndex))
        return newArr

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # self.quickSort(nums, 0, len(nums) - 1)
        # return nums

        # return self.quickSortV2(nums)

        return self.selectionSort(nums)

