# class RandomClass:
#   def __init__(self,data):
#     self.data = data
#     self.str = "Hello"
    
#   def change(self):
#     self.data2 = 12
#     self.data += 2
#   def change2(self):
#     self.data2 += 3
    
# newClass = RandomClass(10)

# newClass.change()
# print(newClass.data2)
# newClass.change2()
# print(newClass.data2)

class MyClass:
  class_var = "This is a class variable"  # Class variable

  def __init__(self):
    self.instance_var = "This is an instance variable"  # Instance variable

  def my_method(self):
    self.another_var = "This is another instance variable"  # Instance variable

obj1 = MyClass()
obj2 = MyClass()

# Accessing class variable
print(MyClass.class_var)  # This will print "This is a class variable"

# Accessing instance variables
print(obj1.instance_var)  # This will print "This is an instance variable"
print(obj2.instance_var)  # This will also print "This is an instance variable" (because it's a separate instance)

# Modifying instance variables
MyClass.class_var = "Modified class var variable"
print(obj1.class_var)  
print(obj2.class_var)