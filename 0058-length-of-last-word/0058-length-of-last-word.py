class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(range(len(s))):
            if s[i] == " ":
                if count == 0:
                    continue
                else:
                    break
            else:
                count+=1
        return count