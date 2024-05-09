def bubble_sort(list_to_sort):
  sorted = False;
  while not sorted:
    sorted = True;
    for i in range(len(list_to_sort)-1):
      if list_to_sort[i] > list_to_sort[i+1]:
        sorted = False;
        temp = list_to_sort[i]
        list_to_sort[i] = list_to_sort[i+1]
        list_to_sort[i+1] = temp;
  
  return list_to_sort;
      
print(bubble_sort(['dddd','aaa','b','c']))
print(bubble_sort([6,5,1,1,12,9,31]))

print([1,2,3,4,5,6,7,8,'hello',10])
