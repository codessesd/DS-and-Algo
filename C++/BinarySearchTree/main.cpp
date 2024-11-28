#include <iostream>
#include "BinarySearchTree.cpp"
using namespace std;

int main()
{
  BinarySearchTree *myTree = new BinarySearchTree();

  myTree->insert(25);
  myTree->insert(19);
  myTree->insert(21);
  myTree->insert(16);
  myTree->insert(18);
  myTree->insert(30);
  myTree->insert(23);
  myTree->insert(22);
  myTree->insert(24);
  myTree->insert(26);
  myTree->insert(15);

  cout << myTree->contains(24) << endl;

  cout << myTree->root->left->right->right->left->data << endl;
  return 0;
}