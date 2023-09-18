class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        n_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n_needle] == needle:
                return i
        return -1