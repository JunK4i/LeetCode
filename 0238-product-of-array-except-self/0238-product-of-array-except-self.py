class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = []
        for i in range(len(nums)):
            if(nums[i]==0):
                zero.append(i)
                continue
            total*=nums[i]

        print(total)
        print(zero)
        ans = []
        for i in range(len(nums)):
            if (nums[i] != 0 and len(zero) != 0) or len(zero) > 1:
                ans.append(0)
            elif nums[i] == 0:
                ans.append(total)
            else:
                ans.append(int(total*(nums[i]**-1)))
        print(ans)        
        return ans