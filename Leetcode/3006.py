from typing import List
class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        i_s = []
        j_s = []
        n = len(s)
        win1 = len(a)
        win2 = len(b)
        
        for i in range(n - win1 + 1):
            if s[i:i + win1] == a:
                i_s.append(i)
                
        for j in range(n - win2 + 1):
            if s[j:j + win2] == b:
                j_s.append(j)
        
        if len(i_s) == 0 or len(j_s) == 0:
            return []
        
        res = []
        i,j = 0, 0
        
        print(i_s)
        print(j_s)

        while i < len(i_s) and j < len(j_s):
            if abs(i_s[i] - j_s[j]) <= k:
                res.append(i_s[i])
                i += 1
            elif j_s[j] - i_s[i] > k:
                i += 1
            else:
                j += 1
            
        return res