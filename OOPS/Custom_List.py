import ctypes

# mostly for interviews to know how the inbuilt functions actually works in the python


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

    # to access the list elements by index we use __getitem__ method that is called when we use the indexing operator [] on the object of the class
    def __getitem__(self, index):
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            return "Index Error: list index out of range"

    # implementing clear() method to clear the list- it basically reintializes the list by creating a new array and resetting the size and capacity
    def clear(self):
        self.size = 0

    # insertion in the list - it insert the element at index and shift the elements to right to make space for the new element
    def insert(self, index, item):
        # check first the capacity is full or not
        if self.size == self.capacity:
            self.__resize(2*self.capacity)
        elif index < 0 or index > self.size:
            return "Index Error: list index out of range"

        # run a loop to shift the elements to right from the end to index to make space for the new element
        # we will start from the size to index
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i-1]

        # now there will be duplicate element at index and index+1
        # so we will insert the new element at index and increase the size by 1
        self.array[index] = item
        self.size += 1

    def remove(self, item):
        #first find the index of the item exist or not
        position=-1
        for i in range(self.size):
            if self.array[i]==item:
                position=i
        if position==-1:
            return "ValueError:list item not found"
        
        #if exist then we will shift the elements to the left from index to end
        for i in range (position,self.size-1):
            self.array[i]=self.array[i+1]
        
        self.size-=1
        

            


list = CustomList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
print(list)  # [1,2,3]
list.remove(2)
print(list)
print(len(list))
