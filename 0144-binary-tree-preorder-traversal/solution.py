# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        current = root

        while current:
            if not current.left:
                preorder.append(current.val)
                
                current = current.right
            else:
                predecessor = current.left

                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if not predecessor.right:
                    preorder.append(current.val)
                    
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    current = current.right

        return preorder

