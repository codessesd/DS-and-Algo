class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self, data=None):
    self.head = None;
    self.tail = None;
    self.length = 0;
    if data is not None:
      self.append(data)
      
  def printList(self):
    if self.length == 0:
      print("Empty List")
      return
    temp = self.head;
    for i in range(self.length):
      print(temp.data)
      temp = temp.next
      
  def get(self, index)->Node:
    if index < 0 or index > self.length-1:
      raise ValueError("Index out of bounds")
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp
      
  def set(self, index, data):
    temp = self.get(index)
    temp.data = data
  
  def insert(self, index, data):
    if index < 0 or index > self.length:
      raise ValueError("Index out of bounds")
    if index == 0:
      self.prepend(data)
      return
    if index == self.length:
      self.append(data)
      return
    newNode = Node(data)
    prev = self.head
    temp = self.head
    for i in range(index):
      prev = temp
      temp = temp.next
    newNode.next = temp
    prev.next = newNode

    self.length += 1

  def append(self, data):
    node = Node(data)
    if self.length == 0:
      self.head = node
      self.tail = node
    self.tail.next = node;
    self.tail = node;
    self.length += 1
      
  def prepend(self,data):
    newNode = Node(data)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head = newNode
    self.length += 1;
    
  def deleteLast(self):
    if self.length == 0: return
    if self.length ==  1:
      self.head = None
      self.tail = None
    else:
      temp = self.head
      while(temp.next.next):
        temp = temp.next
      node_to_delete = temp.next
      temp.next = None
      self.tail = temp
      del node_to_delete
    
    self.length -= 1;
    
  def deleteFirst(self):
    if self.length == 0:
      return 
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      temp = self.head;
      self.head = self.head.next;
      del temp
      
    self.length -= 1
      
  def deleteNode(self, index):
    if index < 0 or index > self.length -1: return print("Index out of bounds")
    if index == 0: return self.deleteFirst()
    if index == self.length - 1: return self.deleteLast()
    
    temp = self.head
    for i in range(index-1):
      temp = temp.next
    node_to_delete = temp.next;
    temp.next = temp.next.next
    del node_to_delete
    self.length -= 1
    
  def reverse(self):
    if self.length < 2: return print("Cannot reverse link less than 2 nodes")
    
    before = None
    current = self.head
    after = current.next
    
    self.head = self.tail
    self.tail = current
    
    for i in range(self.length):
      after = current.next
      current.next = before
      before = current
      current = after
      
    

#Code test**************************************
myLinkedList = LinkedList()
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.prepend(5)
myLinkedList.set(1,9)
myLinkedList.insert(0,10000)
myLinkedList.printList()
myLinkedList.deleteNode(3)
print("-------------")
myLinkedList.reverse()
myLinkedList.printList()