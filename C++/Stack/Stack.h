
class Node
{
public:
  int data;
  Node *next;
  Node(int data);
};

class Stack
{
public:
  Stack(int data);
  void printStack();
  void getTop();
  void getHeight();
  void push(int data);
  int pop();

private:
  Node *top;
  int height;
};