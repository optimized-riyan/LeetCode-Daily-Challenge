# Recursive Approach #
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        count = 0
        string = self.countAndSay(n - 1)
        curr = ""
        
        newSay = ""
        # When the next digit is same, we increment the counter
        # If next digit is different, we add str(count) and current digit to the new string
        for char in string:
            if char != curr:
                newSay += str(count) + curr
                curr = char
                count = 1
            else:
                count += 1
        
        return newSay[1:] + str(count) + curr

# Iterative Approach #
class Solution:
    def countAndSay(self, n: int) -> str:
        say = "1"
        for i in range(1, n):
            curr = ""
            count = ""
            newSay = ""
            
            for char in say:
                if char != curr:
                    newSay += str(count) + curr
                    curr = char
                    count = 1
                else:
                    count += 1
            newSay += str(count) + curr
            say = newSay
        return say