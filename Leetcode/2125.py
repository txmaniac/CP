from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prev = None
        total = 0
        for r in range(len(bank)):
            if not prev:
                prev = bank[r].count("1")
            else:
                curr = bank[r].count("1")
                if curr: 
                    total += curr * prev
                    prev = curr

        return total