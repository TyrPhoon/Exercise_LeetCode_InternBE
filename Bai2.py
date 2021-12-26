#Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, data: str) -> int:
        s = []
        maxx = 0
        for i in data:
            if (i in s) == False:
                s.append(i)
            else:
                dem = s.index(i)
                if dem == len(s):
                    s=[]
                else:
                    s = s[dem+1:]
                s.append(i)
            maxx = max(maxx, len(s))
        return maxx
