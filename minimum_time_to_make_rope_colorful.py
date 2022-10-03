# Noob Approach #

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = 0
        minTime = 0
        
        while i < len(colors) - 1:
            if colors[i] == colors[i + 1]:
                slowest = neededTime[i]
                while i < len(colors) - 1 and colors[i] == colors[i + 1]:
                    # with a continuum of same color balloons, remove all except the one
                    # with the longest time to remove
                    if slowest < neededTime[i + 1]:
                        minTime += slowest
                        slowest = neededTime[i + 1]
                    else:
                        minTime += neededTime[i + 1]
                    i += 1
            else:
                i += 1
        return minTime