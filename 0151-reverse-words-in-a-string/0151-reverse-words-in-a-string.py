class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev = reversed(words)
        print(rev)
        return (" ".join(rev)).strip()