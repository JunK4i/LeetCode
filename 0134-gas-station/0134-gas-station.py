class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        total_cost = 0
        tank = 0
        starting_point = 0
        
        for i in range(n):
            total_gas+=gas[i]
            total_cost+=cost[i]
            tank+=gas[i]-cost[i]

            # if tank<0, starting->i, any number in between will still not work because total gas - totalcost
            # up till that point is negative (means any different starting point till istill result in -ve)
            if tank<0:
                starting_point = i+1
                tank = 0
        # this works because there is only 1 solution, dont have to account for the round trip from idx 0
        if total_gas < total_cost:
            return -1
        else:
            return starting_point