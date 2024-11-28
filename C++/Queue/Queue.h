
class Node
{
public:
  int data;
  Node *next;
  Node(int data);
};

class Queue
{
private:
  Node *first;
  Node *last;
  int length;

public:
  Queue(int data);
  void enqueue(int data);
  int dequeue();

  ~Queue();
};