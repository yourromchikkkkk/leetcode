
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = defaultdict(list)

        for string in strs:
            tempArr = [0] * 26
            print('string', string)
            for char in string:
                tempArr[ord(char) - ord("a")] += 1 
            resDict[tuple(tempArr)].append(string)
        
        return list(resDict.values())

solution = Solution()
testCase = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(testCase))