# three traversals we will usual look at are:
# PREORDER: visit root node first, then recursively do a a preorder traversal of the left subtree.
# followed by a recursive preorder traversal of the right subtree.

# INORDER: we recursively do an inorder traversal on the left subtree, visit the root node,
# and finally do a recursive inorder traversal of the right subtree.

# POSTORDER: we recursively do a postorder traversal of the left subtree and the right subtree
# followed by a visit to the root node.

import operator


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        # go through all the left
        preorder(tree.getLeftChild())
        # then go through all of the right.
        preorder(tree.getRightChild())


# could also put preorder as part of the BinaryTree class.
def preorder_class(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()


# probably better to have preorder as an external function because we rarely want to just go through a BST.

def postordereval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def inorder(tree):
  if tree is not None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())


def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal