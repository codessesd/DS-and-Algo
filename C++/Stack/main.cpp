#include <iostream>
#include "Stack.cpp"
using namespace std;

int main()
{
  Stack *myStack = new Stack(1);
  myStack->push(2);
  myStack->push(3);
  // myStack->pop();
  myStack->push(4);

  myStack->printStack();
  myStack->getHeight();
  myStack->getTop();
  return 0;
}