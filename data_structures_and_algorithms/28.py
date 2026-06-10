class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        needle_len = len(needle)

        idx = 0
        for idx in range(len(haystack) - needle_len + 1):
            if haystack[idx:idx+needle_len] == needle:
                return idx
        return -1

    def strStrv1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        s_idx, e_idx = 0, 1
        while e_idx <= len(haystack):
            diff = e_idx - s_idx
            print(f's_idx = {s_idx}; e_idx = {e_idx}; haystack[s_idx:e_idx] = {haystack[s_idx:e_idx]}; needle[:diff] = {needle[:diff]}')
            # print(f'haystack[s_idx:e_idx] == needle[:diff] = {haystack[s_idx:e_idx] == needle[:diff]}')
            if diff == len(needle) and haystack[s_idx:e_idx] == needle[:diff]:
                return s_idx
            if haystack[s_idx:e_idx] != needle[:diff]:
                s_idx += 1
            e_idx += 1
        return s_idx

testCase = 'hello'
pattern = 'll'
res = Solution().strStr(testCase, pattern)
print(f'res = {res}')