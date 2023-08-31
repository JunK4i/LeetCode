class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate_count = 0
        candidate = 0
        for i in range(len(nums)):
            if candidate_count == 0:
                candidate = nums[i]
                candidate_count+=1
            elif candidate != nums[i]:
                candidate_count-=1
            elif candidate == nums[i]:
                candidate_count+=1
        return candidate
