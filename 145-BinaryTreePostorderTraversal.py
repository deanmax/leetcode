# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Given a binary tree, return the postorder traversal of its nodes' values.

# iterative solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # it's actually a reverse of right-left preorder traverse
        # generate a mirror traverse first
        stack, result = [root], []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        # reverse the mirror traverse to get the preorder traverse
        return result[::-1]
