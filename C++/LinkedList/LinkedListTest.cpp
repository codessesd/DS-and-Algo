#include <gtest/gtest.h>
#include "LinkedList.cpp"

TEST(LinkedListTest, DeleteFirstFromEmptyList)
{
  LinkedList *list;
  list->deleteFirst();
  EXPECT_EQ(list->getLength(), 0);
  EXPECT_EQ(list->getHead(), nullptr);
  EXPECT_EQ(list->getTail(), nullptr);
}

TEST(LinkedListTest, DeleteFirstFromSingleNodeList)
{
  LinkedList *list;
  list->addLast(1);
  list->deleteFirst();
  EXPECT_EQ(list->getLength(), 0);
  EXPECT_EQ(list->getHead(), nullptr);
  EXPECT_EQ(list->getTail(), nullptr);
}

TEST(LinkedListTest, DeleteFirstFromMultiNodeList)
{
  LinkedList *list;
  list->addLast(1);
  list->addLast(2);
  list->addLast(3);
  list->deleteFirst();
  EXPECT_EQ(list->getLength(), 2);
  EXPECT_EQ(list->getHead()->data, 2);
  EXPECT_EQ(list->getTail()->data, 3);
}
