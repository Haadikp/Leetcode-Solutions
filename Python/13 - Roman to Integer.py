class Solution:
    def romanToInt(self,strings:str) -> int:
        roman = {'I':1,'V': 5,'X' : 10,'L' : 50,'C' : 100,'D' : 500,'M' : 1000 }
        result = 0
        prev = 0
        current = 0

        for i in reversed(strings):
            current = roman[i]
            if current < prev:
                result -= current
            else:
                result += current
            prev = current
        return result

