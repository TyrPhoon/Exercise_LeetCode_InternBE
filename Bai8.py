# Baseball Game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scr = []
        for i in ops:
            if i != "D" and i != "C" and i != "+":
                d = int(i)
                scr.append(d)
            elif i == "D":
                k = len(scr)
                d = int(scr[k-1])*2
                scr.append(d)
            elif i == "C":
                scr.remove(scr[len(scr)-1])
            elif i == "+":
                k = len(scr)
                d = int(scr[k-1]) + int(scr[k-2])
                scr.append(d)  
        return sum(scr)