class Node
{
public:
  Node(int data);
  int data;
  Node *prev;
  Node *next;
};

class DoublyLinkedList
{
public:
  DoublyLinkedList(int data);
  void printList();
  void getLength();
  void append(int data);
  void deleteLast();
  void prepend(int data);
  void deleteFirst();
  Node *get(int index);
  bool set(int index, int value);
  bool insert(int index, int data);
  void deleteNode(int index);

private:
  Node *head;
  Node *tail;
  int length;

private:
};