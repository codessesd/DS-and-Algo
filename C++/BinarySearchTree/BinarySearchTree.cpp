#include "BinarySearchTree.h"
#include <iostream>

Node::Node(int data)
{
  this->data = data;
  left = nullptr;
  right = nullptr;
}

BinarySearchTree::BinarySearchTree()
{
  root = nullptr;
}

bool BinarySearchTree::insert(int data)
{
  Node *newNode = new Node(data);
  if (root == nullptr)
  {
    root = newNode;
    return true;
  }

  Node *temp = root;
  while (true)
  {
    if (newNode->data == temp->data)
      return false;

    if (newNode->data < temp->data)
    {
      if (temp->left == nullptr)
      {
        temp->left = newNode;
        return true;
      }
      else
      {
        temp = temp->left;
      }
    }
    else
    {
      if (temp->right == nullptr)
      {
        temp->right = newNode;
        return true;
      }
      else
      {
        temp = temp->right;
      }
    }

    if (temp == nullptr)
    {
      temp = newNode;
      return true;
    }
  }

  return false;
}

bool BinarySearchTree::contains(int data)
{
  Node *temp = root;

  while (temp)
  {
    if (data > temp->data)
      temp = temp->right;
    else if (data < temp->data)
      temp = temp->left;
    else
      return true;
  }
  return false;
}