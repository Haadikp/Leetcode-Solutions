class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl= len(needle)
        flag = 0
        index = -1
        for i,num in enumerate(haystack):
            if num == needle[0]:
                flag = 1
            if flag == 1 :
                if index == -1:
                    if haystack[i:(i+nl)] == needle[0:nl]:
                        index = i

        return index
