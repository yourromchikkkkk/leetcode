from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)

        buckets = [[] for _ in range(len(nums) + 1)]
        for n,c in counter.items():
            buckets[c].append(n)
        
        freqArray = []
        for idx in range(len(nums), 0, -1):
            for num in buckets[idx]:
                freqArray.append(num)
                if len(freqArray) == k:
                    return freqArray

        return freqArray



solution = Solution()
print(solution.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) #[1,2]
print(solution.topKFrequent([7,7], 1)) # [7]
print(solution.topKFrequent([1,1,1,2,2,3], 2)) # [1,2]