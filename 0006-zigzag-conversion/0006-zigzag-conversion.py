class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >=n:
            return s
        matrix = [[] for x in range(numRows)]
        row = 0 
        step = 0
        for i in range(n):
            matrix[row].append(s[i])
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step

        for i in range(numRows):
            matrix[i] = "".join(matrix[i])
        return "".join(matrix)

        



