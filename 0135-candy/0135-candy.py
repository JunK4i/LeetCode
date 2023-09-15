class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for x in ratings]
        right = [1 for x in ratings]

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1

        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
                left[i] = max(left[i],right[i])
        
        return sum(left)
        
      
