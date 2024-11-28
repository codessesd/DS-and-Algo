class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
class BinarySearchTree:
  def __init__ (self):
    self.root = None
  def insert(self,data):
    newNode = Node(data)
    
    if self.root == None:
      self.root = newNode
      return
    temp = self.root
    while(True):
      if data > temp.data:
        temp = temp.right
    
    print(self.root.data)
      
# Code test ************************************************

myBST = BinarySearchTree()
myBST.insert(10)