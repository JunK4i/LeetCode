class Solution:
    def canJump(self, nums: List[int], memo = None) -> bool:
        # 1) Identifying DP: At each point, we can access where it can go next
        # 2) What variables change: Array Position(i) and Distance(d)
        # 3) Clearly express the reccurence relation: 
        #       canStop = (i, n-d > n-i)
        # 4) Identify the base case and constraints(based on variables)
        #       illegal base cases: i > n-1, when d==0 or i==n-1
        # 5) Decide if we go with recursive or back propogation
        # 6) Add memoization
        
        # n = len(nums)
        # d = nums[0]
        # if memo == None:
        #     memo = {}
        # # check if results exists in memo
        # memo_key = tuple(nums)
        # if memo_key in memo:
        #     # print(f"memo:{memo}")
        #     return memo[memo_key]
        # if n == 1:
        #     memo[memo_key] = True
        #     return True
        # if d == 0 and n > 1:
        #     memo[memo_key] = False
        #     return False
        # if d >= n:
        #     memo[memo_key] = True
        #     return True
        # else: 
        #     # try all possible jumps
        #     for i in range(1, d+1):
        #         # print(nums[i:n])
        #         if self.canJump(nums[i:n], memo):
        #             memo[memo_key] = True
        #             return True

        if len(nums) == 1: return True
        pos,jump = 0,0

        for pos in range(10000000):
            # if current jump less than jump position, skip
            if jump > pos + nums[pos]:
                pass
            # update max jump distance
            else:
                jump = pos + nums[pos]
                pos += 1
            # if iteration has reached the pt where, it is farther than max jump recorded, return False
            if pos > jump:
                break
            # if jump more than length
            if jump >= len(nums)-1:
                return True
        return False

        