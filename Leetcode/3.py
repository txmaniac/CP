from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countMap = defaultdict(int)
        n = len(s)
        maxWindow = 0
        left, right = 0, 0

        while left < n and right < n:
            if not countMap[s[right]]:
                countMap[s[right]] += 1
                right += 1

            else:
                maxWindow = max(maxWindow, right - left)
                while countMap[s[right]]:
                    countMap[s[left]] -= 1
                    left += 1

        return max(maxWindow, right - left)