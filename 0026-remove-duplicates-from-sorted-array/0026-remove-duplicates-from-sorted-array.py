class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        l = len(nums)
        for i in range(l):
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                nums[i] =  float('inf')
        nums.sort()
        return len(unique)    