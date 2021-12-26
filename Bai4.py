#Distribute Candies

class Solution:
    def distributeCandies(self, a: List[int]) -> int:
        b =[]
        for i in range(len(a)):
            if(a[i] in b) == False:
                b.append(a[i])
            if(len(b)==len(a)/2): break
        kq = int(min(len(a)/2, len(b)))
        return kq