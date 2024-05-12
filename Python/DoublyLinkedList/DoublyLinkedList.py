class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

class DoublyLinkedList:
  def __init__(self, data = None)-> None:
    if data is None:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      newNode = Node(data)
      self.head = newNode
      self.tail = newNode
      self.length = 1

  def printList(self)->None:
    if self.length == 0:
      print("Empty List")
      return
    temp = self.head
    for i in range(self.length):
      print(temp.data)
      temp = temp.next
  def append(self,data)->None:
    newNode = Node(data)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.prev = self.tail
      self.tail = newNode
    self.length += 1
    
  def deleteLast(self)->None:
    if self.length == 0:
      return
    temp = self.tail
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.tail = self.tail.prev
      self.tail.next = None
    del(temp)
    self.length -= 1
    
  def prepend(self,data)->None:
    newNode = Node(data)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      newNode.next = self.head
      self.head.prev = newNode
      self.head = newNode
    self.length += 1
    
  def deleteFirst(self)->None:
    if self.length == 0:
      return
    temp = self.head
    if self.length == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
      self.head.prev = None
    del(temp)
    self.length -= 1
    
  def get(self, index)->Node:
    if index < 0 or index >= self.length:
      # raise ValueError("Index out of bound for function \"get\"")
      return
    temp =  self.head
    for i in range(index):
      temp = temp.next
    return temp
  
  def set(self,index,data)->bool:
    if index < 0 or index >= self.length:
      # raise ValueError("Index out of bound for function \"set\"")
      return False
    temp = self.get(index)
    temp.data = data
    return True
  
  def insert(self, index, data)->bool:
    if index < 0 or index > self.length:
      # raise ValueError("Index out of bound for function \"set\"")
      return False
    if index == 0:
      self.prepend(data)
      return True
    if index == self.length:
      self.append(data)
      return True
    newNode = Node(data)
    temp = self.get(index)
    newNode.next = temp
    newNode.prev = temp.prev
    temp.prev.next = newNode
    temp.prev = newNode
    self.length += 1
    return True
    
  def deleteNode(self, index):
    if index < 0 or index >= self.length:
      # raise ValueError("Index out of bound for function \"set\"")
      return
    if index == 0:
      self.deleteFirst()
      return
    if index == self.length - 1:
      self.deleteLast()
      return
  
    temp = self.get(index)
    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    del(temp)
    self.length -= 1 