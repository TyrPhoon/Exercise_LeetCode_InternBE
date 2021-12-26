#Hamming Distance

class Solution:
    def hammingDistance(self, a: int, b: int) -> int:
        sa = [0]*32
        sb = [0]*32
        i = 31
        while a > 0:
            sa[i] = a%2
            a = int(a/2)
            i-=1
        j = 31
        while b > 0:
            sb[j] = b%2
            b = int(b/2)
            j-=1
        kq = 0
        for i in range(32):
            if sa[i] != sb[i]:kq+=1
        return kq