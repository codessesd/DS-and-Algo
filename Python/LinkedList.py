class Node:
  def __init__(self, value) -> None:
    self.value = value
    self.next = None
    
class LinkedList:
  def __init__(self, value) -> None:
    node = Node(value)
    self.head = node;
    self.tail = node;
    self.length = 1;
    
  def printList(self):
    temp = self.head;
    for i in range(self.length):
      print(temp.value)
      temp = temp.next
      
  def get():
    pass
  def set():
    pass
  def insert():
    pass
  
  def append(self, value):
    node = Node(value)
    if self.length == 0:
      self.head = node
      self.tail = node
    self.tail.next = node;
    self.tail = node;
    self.length += 1
    
      
  def prepend(self,value):
    pass
  
  def deleteLast():
    pass
  def deleteFist():
    pass
  def insert():
    pass
  def deleteNode():
    pass
  def reverse():
    pass
      
    

#Code test**************************************
myLinkedList = LinkedList(10)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.printList()