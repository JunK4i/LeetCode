class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        num_len = len(nums)
        count = 0
        for i in range(num_len):
            if nums[i] not in num_dict:
                num_dict[nums[i]] = 1
            else:
                num_dict[nums[i]] +=1
                if num_dict[nums[i]] >2:
                    count+=1
                    nums[i] = 10**4 +1
        nums.sort()
        return num_len - count