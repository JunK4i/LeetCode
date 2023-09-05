class Solution:
    def jump(self, nums: List[int]) -> int:
        # at each step find the farthest u can jump and the number of steps. 
        # update indexes that can increase furthest jump
        # When you have reached the end, start from the beginning and find the largest index that can increase
        # max jumps

        n = len(nums)
        reachable = 0
        jumps = {}
        for i in range(n):
            if reachable >= n-1:
                # jumps store the indexes that extend "reachable"
                # j keeps track of jumper index. 
                # within each jump_distance, look for the largest index in jumps{} that can extend reachable
                # repeat until jump_distance < reachable
                j = 0
                keys = list(jumps.keys())
                jump_distance = 0
                jump_count = 0
                while jump_distance < reachable:
                    jump_distance = jumps[j]
                    # filters indexes that are <= the previous jump, and finds the max
                    j = max(filter(lambda x: x <= jump_distance, keys))
                    jump_count+=1
                return jump_count
            if reachable < nums[i]+ i:
                reachable = nums[i]+i
                jumps[i] = reachable
            
        

            