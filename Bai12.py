# Longest Uncommon Subsequence I

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        dem = -1
        if len(a)>len(b):
            for i in range(len(a)):
                for j in range(i,len(a)):
                    s = a[i:j+1]
                    if (s in b) == False: dem = max(dem, len(s))
        else:
            for i in range(len(b)):
                for j in range(i,len(b)):
                    s = b[i:j+1]
                    if (s in a) == False: dem = max(dem, len(s))
        return dem
        

# class Solution:
#     def findLUSlength(self, a: str, b: str) -> int:
#         if a == b: return -1
#         else: return max(len(a),len(b))
        