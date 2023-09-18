class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        remove  = list(filter(lambda x: x!="", words))
        rev = reversed(remove)
        print(remove)
        return (" ".join(rev)).strip()