# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root == None:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root



if __name__ == '__main__':

    root = TreeNode(val = [4,2,7,1,3,6,9])

    sol = Solution()
    sol.invertTree(root)
    print(sol)