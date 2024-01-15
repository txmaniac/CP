from typing import List
from bisect import bisect_left

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def compute_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def kmp_search(text, pattern):
            beautiful_indices = []
            lps = compute_lps(pattern)
            i, j = 0, 0
            while i < len(text):
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                if j == len(pattern):
                    beautiful_indices.append(i - j)
                    j = lps[j - 1]
                elif i < len(text) and pattern[j] != text[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return beautiful_indices

        indices_a = kmp_search(s, a)
        indices_b = kmp_search(s, b)

        beautiful = []
        for i in indices_a:
            p = bisect_left(indices_b, i)
            for j in range(p - 1, p + 2):
                if 0 <= j < len(indices_b) and abs(i - indices_b[j]) <= k:
                    beautiful.append(i)
                    break
                    
        return beautiful