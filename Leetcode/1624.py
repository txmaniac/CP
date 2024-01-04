class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexes = {}
        maxWindow = -1
        for i, ch in enumerate(s):
            if ch not in indexes:
                indexes[ch] = i
            else:
                maxWindow = max(maxWindow, i - indexes[ch] - 1)

        return maxWindow