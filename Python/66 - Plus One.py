class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        print(digits)
        num = 0
        for i in digits:
            num = num * 10 + i
        digits.clear()
        num = num + 1
        for x in str(num):
            digits.append(int(x))
        return digits
