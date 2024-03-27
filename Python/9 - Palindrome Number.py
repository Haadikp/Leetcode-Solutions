class Solution:
    def isPalindrome(self, num):
    
        if num < 0:
            return 0
        temp = num
        reverse = 0
        while temp != 0:
            x = temp % 10
            temp = temp // 10
            reverse = reverse * 10 + x

        return num == reverse
            





