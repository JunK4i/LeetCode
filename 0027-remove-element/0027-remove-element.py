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
        
        n = len(nums)
        m = 0
        for i in range(n):
            if nums[i] == val:
                nums[i] = 51
                m+=1
        nums.sort()
        return n-m