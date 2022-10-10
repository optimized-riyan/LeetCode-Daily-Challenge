class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        n = len(palindrome)
        lengthIsEven = (n % 2 == 0)
        
        palindrome = list(palindrome)
        # The first element we encounter that is not a will be changed to a
        for i in range(n):
            if palindrome[i] != 'a' and (lengthIsEven or i != n // 2):
                palindrome[i] = 'a'
                return "".join(palindrome)
        
        # If the string is of type (a*) or (a*)z(a*), we replace last letter by b
        return "".join(palindrome[:-1]) + "b"