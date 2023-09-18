class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        i = 0
        n_strings = len(strs)

        for i in range(201):
            check = strs[0][0:i]
            # print(check)
            mismatch = False
            for j in range(1,n_strings):
                if strs[j][0:i] != check:
                    mismatch = True
                    break
            if mismatch == False:
                lcp = check
                # print(f"lcp {lcp}")
            else: 
                break
        return lcp

            