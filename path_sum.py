class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        isTrue = False
        # Use preorder traversal and calculate prefix sum of all previous nodes (pSum) #
        def preorder(root: TreeNode, pSum: int):
            nonlocal targetSum
            nonlocal isTrue
            
            if not root:
                return
            pSum += root.val
            if not root.left and not root.right:
                if pSum == targetSum:
                    isTrue = True
                    return
                else:
                    return
            else:
                preorder(root.left, pSum)
                preorder(root.right, pSum)
        
        preorder(root, 0)
        return isTrue