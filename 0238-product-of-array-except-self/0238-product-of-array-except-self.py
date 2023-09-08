class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # this is a hack to deal with the division operation requirement by using exponential -1
        # total = 1
        # zero = []
        # for i in range(len(nums)):
        #     if(nums[i]==0):
        #         zero.append(i)
        #         continue
        #     total*=nums[i]
        # ans = []
        # for i in range(len(nums)):
        #     if (nums[i] != 0 and len(zero) != 0) or len(zero) > 1:
        #         ans.append(0)
        #     elif nums[i] == 0:
        #         ans.append(total)
        #     else:
        #         ans.append(int(total*(nums[i]**-1)))
        # return ans

        # Prefix, Suffix product, ans[i] = pre[i] * suff[i]. effectively removing i from product
        n  = len(nums)
        pre = [1] #contains product every element before i
        suff = [1 for x in nums]
        ans = []

        for i in range(1, n):
            pre.append(pre[i-1] * nums[i-1])
        
        for i in reversed(range (n-1)):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(n):
            ans.append(pre[i] * suff[i])

        return ans

