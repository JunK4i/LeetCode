class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # match = []
        # for i in range (n):
        #     if nums[i] == val:
        #         match.append(nums[i])
        # for num in match:
        #     nums.remove(num)
        #     nums.append(num)
        # k = n-len(match)
        
        n = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == val:
                nums[i] = 51
                n += 1
        nums.sort()
        return l - n