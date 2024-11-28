#include "Queue.h"
#include "climits"

Node::Node(int data)
{
  this->data = data;
  next = nullptr;
}

Queue::Queue(int data)
{
  Node *newNode = new Node(data);
  first = newNode;
  last = newNode;
  length = 1;
}

void Queue::enqueue(int data)
{
  Node *newNode = new Node(data);
  if (length == 0)
  {
    first = newNode;
    last = newNode;
  }
  else
  {
    last->next = newNode;
    last = newNode;
  }

  length++;
}

int Queue::dequeue()
{
  if (length == 0)
    return INT_MIN;

  Node *temp = first;
  int valueToReturn = first->data;
  if (length == 1)
  {
    first = nullptr;
    last = nullptr;
  }
  else
  {
    first = first->next;
  }

  length--;
  delete (temp);
  return valueToReturn;
}

Queue::~Queue()
{
  Node *temp = first;
  while (first)
  {
    first = first->next;
    delete temp;
    temp = first;
  }
}