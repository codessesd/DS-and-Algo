"""
Generate a unit test for a DoublyLinkedList with the following structure.
class Node with self.data, self.prev, self.next
class DoublyLinkedList with self.head, self.tail, self.length
and the following methods: append, prepend, deleteFirst, deleteLast,
get(index)->Node, set(index, data)->bool, insert(index, data)->boo,
deleteNode(index)
"""
import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
     def test_append(self):
       dll = DoublyLinkedList()
       dll.append(1)
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.tail.data, 1)
       dll.append(2)
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.tail.data, 2)
       self.assertEqual(dll.head.next.data, 2)
       self.assertEqual(dll.tail.prev.data, 1)
   
     def test_prepend(self):
       dll = DoublyLinkedList()
       dll.prepend(1)
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.tail.data, 1)
       dll.prepend(2)
       self.assertEqual(dll.head.data, 2)
       self.assertEqual(dll.tail.data, 1)
       self.assertEqual(dll.head.next.data, 1)
       self.assertEqual(dll.tail.prev.data, 2)
   
     def test_deleteFirst(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(2)
       dll.deleteFirst()
       self.assertEqual(dll.head.data, 2)
       self.assertEqual(dll.tail.data, 2)
       self.assertIsNone(dll.head.prev)
       self.assertIsNone(dll.tail.next)
   
     def test_deleteLast(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(2)
       dll.deleteLast()
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.tail.data, 1)
       self.assertIsNone(dll.head.prev)
       self.assertIsNone(dll.tail.next)
   
     def test_deleteNode(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(2)
       dll.append(3)
       dll.deleteNode(1)
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.tail.data, 3)
       self.assertEqual(dll.head.next.data, 3)
       self.assertEqual(dll.tail.prev.data, 1)
   
     def test_get(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(2)
       dll.append(3)
       self.assertEqual(dll.get(0).data, 1)
       self.assertEqual(dll.get(1).data, 2)
       self.assertEqual(dll.get(2).data, 3)
   
     def test_insert(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(3)
       self.assertTrue(dll.insert(1, 2))
       self.assertEqual(dll.head.data, 1)
       self.assertEqual(dll.head.next.data, 2)
       self.assertEqual(dll.tail.data, 3)
   
     def test_set(self):
       dll = DoublyLinkedList()
       dll.append(1)
       dll.append(2)
       self.assertTrue(dll.set(0, 3))
       self.assertEqual(dll.head.data, 3)
       self.assertEqual(dll.tail.data, 2)
   
if __name__ == '__main__':
    unittest.main()