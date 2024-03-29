class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        compare = strs[0]
        length = len(compare)
        for i in strs[1:len(strs)]:
            while length != 0:
                if compare[0:length] == i[0:length]:
                    compare = compare[0:length]
                    break
                else:
                    length -= 1
                    
        return compare[0:length]

