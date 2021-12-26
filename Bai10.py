#Island Perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        tong = 0
        lap = 0
        for i in range(len(grid)):
            tong += grid[i].count(1)
            for j in range(len(grid[i])-1):
                if(grid[i][j] == grid[i][j+1] == 1): lap +=1
        for j in range(len(grid[0])):
            for i in range(len(grid)-1):
                if(grid[i][j] == grid[i+1][j] == 1): lap +=1
        return tong*4-lap*2