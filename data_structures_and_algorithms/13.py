class Solution(object):
    def romanToIntv1(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        idx, previous_val = len(s) - 1, 0
        res = 0

        while idx >= 0:
            current = symbol_dict[s[idx]]
            if current < previous_val:
                res -= current
            else:
                res += current
            previous_val = symbol_dict[s[idx]]
            idx -= 1
        
        return res
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        len_s = len(s)
        res = 0

        for idx in range(len_s):
            if idx + 1 < len_s and symbol_dict[s[idx]] < symbol_dict[s[idx + 1]]:
                res -= symbol_dict[s[idx]]
            else:
                res += symbol_dict[s[idx]]
        
        return res

testCase = "MCMXCIV"
solution = Solution().romanToInt(testCase)
print(solution)