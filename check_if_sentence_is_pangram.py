class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        mapping = {}
        
        for i in range(26):
            mapping[chr(i + 97)] = 0
        
        numZeros = 26
        for char in sentence:
            if mapping[char] == 0:
                numZeros -= 1
            mapping[char] += 1
        
        if numZeros == 0:
            return True
        else:
            return False