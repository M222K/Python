import ctypes


class CustomList():

    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0
        # as list is a dynamic array , we will create array for the list using ctypes module
        self.array = self.__create_array(self.capacity)

    def __create_array(self, capacity):
        # this will create a python ctype array object-it is a refrential array which store the refrences of the objects in the list
        return (capacity*ctypes.py_object)()

    def __resize(self, newCapacity):
        newArray = self.__create_array(newCapacity)
        # copy all the items of old array to new array
        for i in range(self.size):
            newArray[i] = self.array[i]
        # then change the reference of old array to new array
        self.array = newArray
        self.capacity = newCapacity

    def append(self, item):
        if self.size == self.capacity:
            self.__resize(2*self.capacity)

        self.array[self.size] = item
        self.size += 1

    def __len__(self):
        return self.size
    # whenever we call len() function on object this dunder method is called , so we can modify it sbehaviour as per our need

    def __str__(self):
        # this method is called when we print the object of the class
        # we can modify it to return the string representation of the object as per our need
        output = ""
        for i in range(self.size):
            output += str(self.array[i])+","
        return "["+output[:-1]+"]"

    def pop(self):
        # check whether the list is empty
        if self.size == 0:
            raise IndexError("pop from empty list")

        # last index will be size-1
        popped_item = self.array[self.size-1]
        # to remove this from the lsit we will unlink the list from this end and decrease the size refrence by 1
        self.size = self.size-1
        return popped_item
    
    

list = CustomList()
list.append(1)
list.append(2)
list.append(3)
print(list)  # [1,2,3]

list.pop()
print(list)
list.pop()
print(list)
list.pop()
print(list)
print(list.pop())
