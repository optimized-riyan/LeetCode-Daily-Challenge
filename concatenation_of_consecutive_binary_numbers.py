class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binNum = ""
        for i in range(1, n + 1):
            binNum += bin(i)[2:]
        binNum = "0b" + binNum
        return int(binNum, 2) % (10**9 + 7)
