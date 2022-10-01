# Dynamic Programming #

class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: string is immediately invalid if it starts with 0
        if s[0] == '0':
            return 0
        
        combs = [1] * len(s)
        
        # For general cases:
        # combs[i] =    num{previous substring's combinations: combs[i - 1] if s[i] is not 0}
        #           +   num{previous to previous substring's combinations: combs[i - 2]
        #                   if the double digit number is between 10 and 26(since 01 to
        #                   09 will also be considered double digit numbers)}
        # Edge case: i = 1

        for i in range(1, len(s)):
            combs[i] = 0 if s[i] == '0' else combs[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                combs[i] += combs[i - 2 if i > 1 else 0]
        
        return combs[-1]