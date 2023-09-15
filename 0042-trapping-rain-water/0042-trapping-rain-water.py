class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = []
        right = []
        max_h = 0
        for i in range(n):
            if height[i]>max_h:
                max_h = height[i]
            left.append(max_h)
        max_h = 0
        for i in reversed(range(n)):
            if height[i] > max_h:
                max_h = height[i]
            right.insert(0,max_h)

        water = 0
        for i in range(n):
            amt = min(right[i],left[i]) - height[i]
            if amt > 0:
                water += amt
        return water
            


