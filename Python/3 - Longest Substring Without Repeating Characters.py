class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 0
        current = ""

        for i in s:
            if i not in current:
                current += i
                if len(current) > longest:
                    longest = len(current)
            else:
                index = current.index(i)
                current = current[index + 1:] + i
        return longest
