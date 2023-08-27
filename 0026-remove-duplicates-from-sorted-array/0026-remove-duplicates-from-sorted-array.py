class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        l = len(nums)
        dup_count = 0
        for i in range(l):
            if nums[i] not in unique:
                unique.append(nums[i])
            else:
                nums[i] = 101
        nums.sort()
        return len(unique)    