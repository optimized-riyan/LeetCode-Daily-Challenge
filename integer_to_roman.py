# Hard coded #

class Solution:
    def intToRoman(self, num: int) -> str:
        letters = ["I", "V", "X", "L", "C", "D", "M"]
        roman = ""
        
        # div = 1000
        mul = num // 1000
        num %= 1000
        roman = "M" * mul
        
        # div = 100:
        mul = num // 100
        num %= 100
        if mul == 9:
            roman += "CM"
        elif 1 <= mul <= 3:
            roman += "C" * mul
        elif mul == 4:
            roman += "CD"
        elif 5 <= mul <= 8:
            roman += "D" + "C" * (mul - 5)
            
        # div = 10:
        mul = num // 10
        num %= 10
        if mul == 9:
            roman += "XC"
        elif 1 <= mul <= 3:
            roman += "X" * mul
        elif mul == 4:
            roman += "XL"
        elif 5 <= mul <= 8:
            roman += "L" + "X" * (mul - 5)
            
        # div = 1:
        mul = num
        if mul == 9:
            roman += "IX"
        elif 1 <= mul <= 3:
            roman += "I" * mul
        elif mul == 4:
            roman += "IV"
        elif 5 <= mul <= 8:
            roman += "V" + "I" * (mul - 5)
        
        return roman