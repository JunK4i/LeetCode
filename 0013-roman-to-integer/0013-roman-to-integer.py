class Solution:
    def romanToInt(self, s: str) -> int:
        # total = 0 
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # i=0
        # while i < len(s):
        #     char = s[i]
        #     if i < len(s)-1:
        #         if char == "I" and (s[i+1] == "V" or s[i+1] == "X"):
        #             total += dic[s[i+1]] -1
        #             i+=2
        #         elif char == "X" and (s[i+1] == "L" or s[i+1] == "C"):
        #             total += dic[s[i+1]] - 10
        #             i+=2
        #         elif char == "C" and (s[i+1] == "D" or s[i+1] == "M"):
        #             total += dic[s[i+1]] - 100
        #             i+=2
        #         else:
        #             total += dic[s[i]]
        #             i+=1
        #     else:
        #         total += dic[s[i]]
        #         i+=1
        # return total

        a = []
        for char in s:
            a.append(dic[char])
        
        for i in range(len(a)-1):
            if a[i] < a[i+1]:
                a[i] = -a[i]
        return sum(a)