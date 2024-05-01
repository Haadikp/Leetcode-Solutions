class Solution:
    def lengthOfLastWord(self,s:str) -> int:
        count = 0
        list1 = s.split(" ")
        for num,i in enumerate(list1):
            if i != "":
                count = num
        return len(list1[count])
