#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # Calculate the net gas available at each station (gas - cost)
    net_gas = [g - c for g, c in zip(gas, cost)]
    print(net_gas)
    
    # If the total net gas available is negative, there is no solution
    if sum(net_gas) < 0:
        return -1
    
    # Starting from the first station, check if a full circuit can be completed
    tank = 0
    start = 0
    for i, g in enumerate(net_gas):
        tank += g
        if tank < 0:
            # If the tank becomes negative, reset it and start from the next station
            tank = 0
            start = i + 1
    
    # If the loop completes without returning, the starting station is valid
    return start

# @lc code=end

