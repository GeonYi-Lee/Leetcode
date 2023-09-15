from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        if (len(a-b) == 0) & (len(b-a) == 0) :
            return True
        else:
            return False
        
