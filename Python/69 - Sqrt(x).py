class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        i = 0
        if x < 0:
            x = (-1) * x
        if x == 0:
            root = 0
        elif x == 1:
            root = 1
        else:
            while i*i <= x:
                i += 1
            if i * i == x:
                root = i
            else:
                i -= 1
                root = i
              
        return root
