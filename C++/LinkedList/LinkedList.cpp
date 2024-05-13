#include <iostream>
#include <string>
using namespace std;

// A node in a linked list********************
class Node
{
public:
  Node(int value)
  {
    this->value = value;
    next = nullptr;
  }
  int value;
  Node *next;
};
// The linked list******************************
class LinkedList
{
public:
  LinkedList(int value)
  {
    Node *newNode = new Node(value);
    head = newNode;
    tail = newNode;
    length++;
  }
  void printList()
  {
    if (length == 0)
    {
      cout << "Empty Linked List";
      return;
    }
    Node *temp = head;
    while (temp)
    {
      cout << temp->value << endl;
      temp = temp->next;
    }
  }
  void getHead()
  {
    cout << head->value << endl;
  }
  void getTail()
  {
    cout << tail->value << endl;
  }
  void getLength()
  {
    cout << "Length: " << length << endl;
  }

  void append(int value)
  {
    Node *newNode = new Node(value);
    if (length == 0)
    {
      head = newNode;
      tail = newNode;
    }
    else
    {
      tail->next = newNode;
      tail = newNode;
    }
    length++;
  }

  void deleteLast()
  {
    if (length == 0)
      return;

    if (length == 1)
    {
      delete head;
      head = nullptr;
      tail = nullptr;
    }
    else
    {
      Node *prev = head;
      Node *next = head;
      while (next->next)
      {
        prev = next;
        next = next->next;
      }
      tail = prev;
      tail->next = nullptr;
      delete (next);
    }
    length--;
  }

  void prepend(int value)
  {
    Node *newNode = new Node(value);
    if (length == 0)
    {
      newNode->next = nullptr;
      head = newNode;
      tail = newNode;
    }
    else
    {
      newNode->next = head;
      head = newNode;
    }
    length++;
  }

  void deleteFirst()
  {
    if (length == 0)
      return;
    Node *temp = head;
    if (length == 1)
    {
      head = nullptr;
      tail = nullptr;
    }
    else
    {
      head = head->next;
    }
    delete (temp);
    length--;
  }

  Node *get(int index)
  {
    if (!validIndex(index))
      return nullptr;
    Node *temp = head;
    int i = 0;
    while (i != index)
    {
      temp = temp->next;
      i++;
    }
    return temp;
  }

  bool set(int index, int value)
  {
    if (index < 0 || index > length - 1)
      return false;

    Node *temp = head;
    int i = 0;
    while (i != index)
    {
      temp = temp->next;
      i++;
    }
    temp->value = value;

    return true;
  }

  bool insert(int index, int value)
  {
    if (index < 0 || index > length)
    {
      cout << "Invalid Index" << endl;
      return false;
    }

    if (index == 0)
    {
      prepend(value);
      return true;
    }

    if (index == length)
    {
      append(value);
      return true;
    }

    Node *newNode = new Node(value);
    Node *prev = get(index - 1);
    newNode->next = prev->next;
    prev->next = newNode;
    length++;
    return true;
  }

  void deleteNode(int index)
  {
    if (!validIndex(index))
      return;

    if (index == 0)
      return deleteFirst();

    if (index == length - 1)
      return deleteLast();

    Node *prev = get(index - 1);
    Node *temp = prev->next;
    prev->next = temp->next;
    delete temp;

    length--;
  }

  void reverse()
  {
    if (length < 2)
      return;

    Node *temp = head;
    head = tail;
    tail = temp;

    Node *after = temp->next;
    Node *before = nullptr;

    for (int i = 0; i < length; i++)
    {
      after = temp->next;
      temp->next = before;
      before = temp;
      temp = after;
    }
  }

  ~LinkedList()
  {
    Node *temp = head;
    while (head)
    {
      head = head->next;
      delete temp;
      temp = head;
    }
  }

private:
  Node *head;
  Node *tail;
  int length;
  bool validIndex(int index)
  {
    if (index < 0 || index > length - 1)
    {
      cout << "Error! Index out of bounds" << endl;
      return false;
    }
    return true;
  }

  Node *nodeAtIndex(int index)
  {
    Node *temp = head;
    int i = 0;
    while (i != index)
    {
      temp = temp->next;
      i++;
    }
    return temp;
  }
};

int main()
{
  LinkedList *myList = new LinkedList(200);
  // myList->deleteNode(0);
  // myList->deleteNode(0);
  // myList->deleteFirst();
  // myList->deleteLast();
  myList->append(300);
  myList->prepend(100);
  myList->append(400);
  myList->append(500);
  myList->append(600);
  // myList->set(0, 12);
  // myList->insert(0, 12);

  // myList->reverse();
  myList->printList();
  return 0;
}
