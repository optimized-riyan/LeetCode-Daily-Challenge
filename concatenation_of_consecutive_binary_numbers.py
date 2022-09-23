class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binNum = ""     # Create enmpty string
        for i in range(1, n + 1):
            binNum += bin(i)[2:]    # bin() creates binary num. lead by 0b, [2:] removes 0b
        binNum = "0b" + binNum      # add 0b to represent it is binary
        return int(binNum, 2) % (10**9 + 7)
