import unittest
from LinkedList import Node, LinkedList

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.length, 1)
        ll.append(2)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 2)
        self.assertEqual(ll.length, 2)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.length, 1)
        ll.prepend(2)
        self.assertEqual(ll.head.data, 2)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.length, 2)

    def test_get(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.get(0).data, 1)
        self.assertEqual(ll.get(1).data, 2)
        self.assertEqual(ll.get(2).data, 3)
        with self.assertRaises(ValueError):
            ll.get(-1)
        with self.assertRaises(ValueError):
            ll.get(3)

    def test_set(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.set(0, 4)
        self.assertEqual(ll.head.data, 4)
        ll.set(2, 6)
        self.assertEqual(ll.tail.data, 6)

    def test_insert(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.insert(0, 4)
        self.assertEqual(ll.head.data, 4)
        self.assertEqual(ll.length, 4)
        ll.insert(2, 5)
        self.assertEqual(ll.get(2).data, 5)
        self.assertEqual(ll.length, 5)
        with self.assertRaises(ValueError):
            ll.insert(-1, 6)
        with self.assertRaises(ValueError):
            ll.insert(6, 6)

    def test_deleteLast(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.deleteLast()
        self.assertEqual(ll.tail.data, 2)
        self.assertEqual(ll.length, 2)
        ll.deleteLast()
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.length, 1)
        ll.deleteLast()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_deleteFirst(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.deleteFirst()
        self.assertEqual(ll.head.data, 2)
        self.assertEqual(ll.length, 2)
        ll.deleteFirst()
        self.assertEqual(ll.head.data, 3)
        self.assertEqual(ll.length, 1)
        ll.deleteFirst()
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertEqual(ll.length, 0)

    def test_deleteNode(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.deleteNode(2)
        self.assertEqual(ll.get(2).data, 4)
        self.assertEqual(ll.length, 4)
        ll.deleteNode(0)
        self.assertEqual(ll.head.data, 2)
        self.assertEqual(ll.length, 3)
        ll.deleteNode(2)
        self.assertEqual(ll.tail.data, 4)
        self.assertEqual(ll.length, 2)

    def test_reverse(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)
        ll.reverse()
        self.assertEqual(ll.head.data, 5)
        self.assertEqual(ll.tail.data, 1)
        self.assertEqual(ll.get(1).data, 4)
        self.assertEqual(ll.get(2).data, 3)
        self.assertEqual(ll.get(3).data, 2)
        self.assertEqual(ll.length, 5)

if __name__ == '__main__':
    unittest.main()
