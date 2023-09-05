class Solution:
    def jump(self, nums: List[int]) -> int:
        # at each step find the farthest u can jump and the number of steps. 
        # if you can jump further with less steps, update count
        n = len(nums)
        reachable = 0
        jump_count = 0
        jumps = {}
        for i in range(n):
            if reachable >= n-1:
                print(nums)
                print(f"returning i:{i}, reachable:{reachable}, jump_count{jump_count}")
                print(jumps)
                j = 0
                keys = list(jumps.keys())
                jump_distance = 0
                jump_count = 0
                while jump_distance < reachable:
                    jump_distance = jumps[j]
                    j = max(filter(lambda x: x <= jump_distance, keys))
                    jump_count+=1
                    print(f"j:{j},jump_d:{jump_distance}")
                    print(max(filter(lambda x: x <= jump_distance, keys)))
                return jump_count
            if reachable < nums[i]+ i:
                reachable = nums[i]+i
                jump_count+=1
                jumps[i] = reachable
            else:
                continue
        
        print(f"i:{i}, reachable:{reachable}, jump_count{jump_count}")

            