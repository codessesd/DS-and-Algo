#include <iostream>
#include "Stack.h"
using namespace std;

Node::Node(int data)
{
  this->data = data;
  next = nullptr;
}

Stack::Stack(int data)
{
  Node *newNode = new Node(data);
  top = newNode;
  height = 1;
}

void Stack::printStack()
{
  Node *temp = top;
  while (temp)
  {
    cout << temp->data << endl;
    temp = temp->next;
  }
}

void Stack::getTop()
{
  if (height <= 0)
    return;
  cout << "Top: " << top->data << endl;
}

void Stack::getHeight()
{
  cout << "Height: " << height << endl;
}

void Stack::push(int data)
{
  Node *newNode = new Node(data);
  newNode->next = top;
  top = newNode;
  height++;
}

int Stack::pop()
{
  if (height == 0)
  {
    return INT_MIN;
  }

  Node *temp = top;
  int valueToReturn;
  valueToReturn = temp->data;

  top = top->next;
  delete (temp);
  height--;
  return valueToReturn;
}