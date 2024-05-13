import unittest
from DoublyLinkedList import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_append(self):
      dll = DoublyLinkedList()
      dll.append(1)
      self.assertEqual(dll.head.data, 1)
      self.assertEqual(dll.tail.data, 1)
      self.assertEqual(dll.length, 1)
      dll.append(2)
      self.assertEqual(dll.head.data, 1)
      self.assertEqual(dll.tail.data, 2)
      self.assertEqual(dll.length, 2)

    def test_prepend(self):
      dll = DoublyLinkedList()
      dll.prepend(1)
      self.assertEqual(dll.head.data, 1)
      self.assertEqual(dll.tail.data, 1)
      self.assertEqual(dll.length, 1)
      dll.prepend(2)
      self.assertEqual(dll.head.data, 2)
      self.assertEqual(dll.tail.data, 1)
      self.assertEqual(dll.length, 2)

    def test_get(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      self.assertEqual(dll.get(0).data, 1)
      self.assertEqual(dll.get(1).data, 2)
      self.assertEqual(dll.get(2).data, 3)
      self.assertIsNone(dll.get(-1))
      self.assertIsNone(dll.get(3))

    def test_set(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      self.assertTrue(dll.set(0, 4))
      self.assertEqual(dll.head.data, 4)
      self.assertTrue(dll.set(2, 6))
      self.assertEqual(dll.tail.data, 6)
      self.assertFalse(dll.set(-1, 7))
      self.assertFalse(dll.set(3, 7))

    def test_insert(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      self.assertTrue(dll.insert(0, 4))
      self.assertEqual(dll.head.data, 4)
      self.assertEqual(dll.length, 4)
      self.assertTrue(dll.insert(2, 5))
      self.assertEqual(dll.get(2).data, 5)
      self.assertEqual(dll.length, 5)
      self.assertFalse(dll.insert(-1, 6))
      self.assertFalse(dll.insert(6, 6))

    def test_deleteLast(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      dll.deleteLast()
      self.assertEqual(dll.tail.data, 2)
      self.assertEqual(dll.length, 2)
      dll.deleteLast()
      self.assertEqual(dll.tail.data, 1)
      self.assertEqual(dll.length, 1)
      dll.deleteLast()
      self.assertIsNone(dll.head)
      self.assertIsNone(dll.tail)
      self.assertEqual(dll.length, 0)

    def test_deleteFirst(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      dll.deleteFirst()
      self.assertEqual(dll.head.data, 2)
      self.assertEqual(dll.length, 2)
      dll.deleteFirst()
      self.assertEqual(dll.head.data, 3)
      self.assertEqual(dll.length, 1)
      dll.deleteFirst()
      self.assertIsNone(dll.head)
      self.assertIsNone(dll.tail)
      self.assertEqual(dll.length, 0)

    def test_deleteNode(self):
      dll = DoublyLinkedList()
      dll.append(1)
      dll.append(2)
      dll.append(3)
      dll.append(4)
      dll.append(5)
      dll.deleteNode(1)
      self.assertEqual(dll.get(1).data, 3)
      self.assertEqual(dll.length, 4)
      dll.deleteNode(0)
      self.assertEqual(dll.head.data, 3)
      self.assertEqual(dll.length, 3)
      dll.deleteNode(2)
      self.assertEqual(dll.tail.data, 4)
      self.assertEqual(dll.length, 2)
      dll.deleteNode(-1)
      self.assertEqual(dll.length, 2)
      dll.deleteNode(2)
      self.assertEqual(dll.length, 2)

if __name__ == '__main__':
    unittest.main()
