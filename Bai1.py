#Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dem = 0
        for i in jewels:
            dem += stones.count(i)
        return dem