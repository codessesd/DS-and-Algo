#include "DoublyLinkedList.h"
#include <iostream>
using namespace std;

Node::Node(int data)
{
  this->data = data;
  prev = nullptr;
  next = nullptr;
}

DoublyLinkedList::DoublyLinkedList(int data)
{
  Node *newNode = new Node(data);
  head = newNode;
  tail = newNode;
  length = 1;
}

void DoublyLinkedList::append(int data)
{
  Node *newNode = new Node(data);
  if (length == 0)
  {
    head = newNode;
    tail = newNode;
  }
  else
  {
    newNode->prev = tail;
    tail->next = newNode;
    tail = newNode;
  }
  length++;
}

void DoublyLinkedList::deleteLast()
{
  if (length == 0)
    return;
  Node *temp = tail;
  if (length == 1)
  {
    head = nullptr;
    tail = nullptr;
  }
  else
  {
    tail = tail->prev;
    tail->next = nullptr;
  }
  delete (temp);
  length--;
}

void DoublyLinkedList::prepend(int data)
{
  Node *newNode = new Node(data);
  if (length == 0)
  {
    head = newNode;
    tail = newNode;
  }
  else
  {
    newNode->next = head;
    head->prev = newNode;
    head = newNode;
  }
  length++;
}

void DoublyLinkedList::deleteFirst()
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
    head->prev = nullptr;
  }
  delete (temp);
  length--;
}

Node *DoublyLinkedList::get(int index)
{
  if (index < 0 || index >= length)
  {
    cout << "Invalid index for method \"get\"" << endl;
    return nullptr;
  }

  Node *temp = head;
  for (int i = 0; i < index; i++)
    temp = temp->next;

  return temp;
}

bool DoublyLinkedList::set(int index, int data)
{
  if (index < 0 || index >= length)
  {
    cout << "Invalid index for method \"set\"" << endl;
    return false;
  }

  Node *temp = head;
  for (int i = 0; i < index; i++)
    temp = temp->next;
  temp->data = data;
  return true;
}

bool DoublyLinkedList::insert(int index, int value)
{
  if (index < 0 || index > length)
  {
    cout << "Invalid index for method \"set\"" << endl;
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
  Node *temp = get(index);
  newNode->prev = temp->prev;
  newNode->next = temp;
  temp->prev->next = newNode;
  temp->prev = newNode;
  length++;
  return true;
}

void DoublyLinkedList::deleteNode(int index)
{
  if (index < 0 || index >= length)
  {
    cout << "Invalid index for method \"deleteNode\"" << endl;
    return;
  }
  if (index == 0)
  {
    deleteFirst();
    return;
  }
  if (index == length - 1)
  {
    deleteLast();
    return;
  }
  Node *temp = get(index);
  temp->prev->next = temp->next;
  temp->next->prev = temp->prev;
  delete (temp);
  length--;
}