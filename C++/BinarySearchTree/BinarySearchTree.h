class Node
{
public:
  int data;
  Node *left;
  Node *right;
  Node(int data);
};

class BinarySearchTree
{
public:
  BinarySearchTree();
  bool insert(int data);
  bool contains(int data);

  void destroy(Node *currentNode)
  {
    if (currentNode == nullptr)
      return;
    if (currentNode->left)
      destroy(currentNode->left);
    if (currentNode->right)
      destroy(currentNode->right);
    delete currentNode;
  }

  ~BinarySearchTree() { destroy(root); }

  // private:
  Node *root;
};