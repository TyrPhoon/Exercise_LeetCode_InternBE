#Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        avgg = []
        count = []
        self.avg(root,0,avgg,count)
        for i in range(len(avgg)):
            avgg[i] /= count[i]
        return avgg
    def avg(self, root : Optional[TreeNode], i : int, avgg : List[float] , count : List[int] ):
        if (root == None): return
        if (i < len(avgg)):
            avgg[i] += root.val
            count[i] +=1
        else:
            avgg.append(root.val)
            count.append(1)
        self.avg(root.left,i+1,avgg,count)
        self.avg(root.right,i+1,avgg,count)