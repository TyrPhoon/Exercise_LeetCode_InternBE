# Reshape the Matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if r*c != m*n: return(mat)
        k =[]
        d = []
        for i in range(m*n):
            d.append(mat[int(i/n)][i%n])
            if ((i+1) % c) == 0:
                tam = d.copy()
                k.append(tam)
                d.clear()
        return(k)