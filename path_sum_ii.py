class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        answers = []
        
        def inorder(root: TreeNode, pSum: int, storage: List[int]):
            if not root:
                return None
            
            storage.append(root.val)
            pSum += root.val
            
            if root.left == None and root.right == None:
                if pSum == target:
                    answers.append(storage)
            else:
                inorder(root.left, pSum, storage[:])
                inorder(root.right, pSum, storage[:])
            
        inorder(root, target, [])
        
        return answers