# Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        d = len(s)
        for i in range(int(d/2)):
            t = s[i]
            s[i] = s[d-1-i]
            s[d-1-i] = t