"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1 = p
        q1 = q
        depth_p=1
        while p1.parent is not None:
            depth_p +=1 
            p1 = p1.parent

        depth_q=1
        while q1.parent is not None:
            depth_q += 1
            q1 = q1.parent

        diff = depth_p - depth_q
        if diff > 0:
            # p is deeper
            for i in range(diff):
                p = p.parent
        else:
            for i in range(-1 * diff):
                q = q.parent
        
        while p != q:
            p =p.parent
            q=q.parent
        return p


        

        
        