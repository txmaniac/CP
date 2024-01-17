from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for word in strs:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - ord('a')] += 1

            hash[tuple(temp)].append(word)

        return hash.values()