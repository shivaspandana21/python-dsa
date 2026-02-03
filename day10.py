# quick sort usimg recursion
def quick_sort(arr):
    if len(arr) <= 1:   
        return arr
    pivot = arr[0]     
    left = []
    right = []
    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [pivot] + quick_sort(right)


print(quick_sort([5, 3, 8, 4, 2]))
print(quick_sort([5,9,8,3,6,2,1]))

"""Class: A class is a blueprint or template used to create objects. It defines properties (data) and methods (functions).

Object: An object is a real instance of a class. It uses the properties and methods defined in the class.
Difference between Class and Object

Class: A class is a blueprint or template. It does not occupy memory.

Object: An object is created from a class. It occupies memory.

Class: Defines properties and methods.

Object: Uses those properties and methods.

Class: Example Car

Object: Example BMW, Audi

Use of Constructor

A constructor is used to initialize (assign values to) an object when it is created.

It runs automatically when an object is created.

It helps in setting initial values for variables of a class.

Example:
When a Student object is created, a constructor can set the student’s name and roll number.
#constructor creates memory
self define function

"""


#class and object
class A:
    a=10
    b='hi'
def main():
    ob=A()
    ob.value()
    print(f"a={ob.a} and b={ob.b}")

main()

#class and object
class A:
    def value(self):
        self.a=10
        self.b="hii"
def main():
    ob=A()
    ob.value()
    print(f"a={ob.a} and b={ob.b}")

main()
#define a class named operation ,declare two varaibles a  and b inside,define two member functions of class->
#add #and product.make  a user menu driven program which returns the sum of two user input numbers,if the 
# user choice is 'a' and returns the product of two user input numbers,if the user choice is 'b'.

class Operation:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
            return self.a+self.b
        
    def pro(self):
            return self.a*self.b

def main():
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    ob=Operation(a,b)
    print("enter your choice")
    print(f"A for adding \n B for muliplication")
    choice=input("enter choice ")
    
    if choice=='A':
         print("result is :",ob.sum())
    elif choice=='B':
         print("result is :",ob.pro())
    else:
         print("Invalid choice")
         
main()

# Linked list: A linked list is a linear data structure used to store a collection of elements (called nodes) where each node is connected to the next one using a link (pointer/reference).
# ["A"| ]  ["B"| ]  ["C"| ]  ["D"| ]  ["E"| null]
# first node is called "Head".

# in order creating the reference and passing it we will be using the "class".

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None
    


    
    def insert_at_last(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        current_node = self.head

        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node

    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("Null")


li = Linked_list()
li.insert_at_last("A")
# li.insert_at_last("B")
# li.insert_at_last("C")
print("LinkedList: ")
li.print_List()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete at first
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    # Delete at end
    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete at middle
    def delete_middle(self):
        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = slow.next

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main program
ll = LinkedList()

# Insert 7 elements
for i in range(1, 8):
    ll.insert(i)

print("After inserting 7 elements:")
ll.display()

# Delete first
ll.delete_first()
print("After deleting first element:")
ll.display()

# Delete middle
ll.delete_middle()
print("After deleting middle element:")
ll.display()

# Delete end
ll.delete_end()
print("After deleting last element:")
ll.display()

# Linked list: A linked list is a linear data structure used to store a collection of 
# elements (called nodes) where each node is connected to the next one using a link (pointer/reference).
# ["A"| ]  ["B"| ]  ["C"| ]  ["D"| ]  ["E"| null]
# first node is called "Head".

# in order creating the reference and passing it we will be using the "class".

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        new_node.next = self.head   # assigning the new nodes' next value of existing head
        self.head = new_node        #updating the head value, new node becomes the head
        
    def insert_at_middle(self,data,position):       # after any value
        new_node = Node(data)

        current_node = self.head

        if current_node:
            while current_node:
                if current_node.data == position:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                else:
                    current_node = current_node.next
            print("Position element not found")
        else:
            print("Position element not found")

    def insert_at_last(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        current_node = self.head

        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node

    def deletion_at_beginning(self):
        self.head = self.head.next

    def deletion_at_middle(self,value):
        current_node = self.head

        if current_node:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next


    def deletion_at_last(self):
        # if not empty
        current_node = self.head

        while current_node.next:
            if current_node.next.next == None:
                current_node.next = None
                return
            else:
                current_node = current_node.next
            


    
    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("None")


li = Linked_list()
li.insert_at_last("A")
li.insert_at_middle(1,'A')
li.insert_at_last("B")
li.insert_at_last("C")
li.insert_at_begin(0)
li.deletion_at_beginning()
li.deletion_at_middle('B')
li.deletion_at_last()

print("LinkedList: ")
li.print_List()

#detect cycle


# Linked list: A linked list is a linear data structure used to store a collection of elements (called nodes) where each node is connected to the next one using a link (pointer/reference).
# ["A"| ]  ["B"| ]  ["C"| ]  ["D"| ]  ["E"| null]
# first node is called "Head".

# in order creating the reference and passing it we will be using the "class".

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        new_node.next = self.head   # assigning the new nodes' next value of existing head
        self.head = new_node        #updating the head value, new node becomes the head
        
    def insert_at_middle(self,data,position):       # after any value
        new_node = Node(data)

        current_node = self.head

        if current_node:
            while current_node:
                if current_node.data == position:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                else:
                    current_node = current_node.next
            print("Position element not found")
        else:
            print("Position element not found")

    def insert_at_last(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        current_node = self.head

        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node

    def deletion_at_beginning(self):
        self.head = self.head.next

    def deletion_at_middle(self,value):
        current_node = self.head

        if current_node:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next


    def deletion_at_last(self):
        # if not empty
        current_node = self.head

        while current_node.next:
            if current_node.next.next == None:
                current_node.next = None
                return
            else:
                current_node = current_node.next
            


    
    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("None")
    



li = Linked_list()
li.insert_at_last("A")
li.insert_at_middle(1,'A')
li.insert_at_last("B")
li.insert_at_last("C")
li.insert_at_begin(0)
li.deletion_at_beginning()
li.deletion_at_middle('B')
li.deletion_at_last()


print("LinkedList: ")
li.print_List()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at_middle(self,data,position):
        new_node = Node(data)
        current_node = self.head
        if current_node:
            while current_node:
                if current_node.data == position:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                else:
                    current_node = current_node.next
            print("Position element not found")
        else:
            print("Position element not found")

    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def deletion_at_beginning(self):
        self.head = self.head.next

    def deletion_at_middle(self,value):
        current_node = self.head
        if current_node:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next

    def deletion_at_last(self):
        current_node = self.head
        if current_node is None:
            return
        if current_node.next is None:
            self.head = None
            return
        while current_node.next:
            if current_node.next.next is None:
                current_node.next = None
                return
            else:
                current_node = current_node.next

    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("None")

    # Corrected detect_cycle method
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle found
        return False  # No cycle


# Create linked list and perform operations
li = Linked_list()
li.insert_at_last("A")
li.insert_at_middle(1,'A')
li.insert_at_last("B")
li.insert_at_last("C")
li.insert_at_begin(0)
li.deletion_at_beginning()
li.deletion_at_middle('B')
li.deletion_at_last()

print("LinkedList: ")
li.print_List()

# Check for cycle
print("Cycle detected?", li.detect_cycle())


# Linked list: A linked list is a linear data structure used to store a collection of elements (called nodes) where each node is connected to the next one using a link (pointer/reference).
# ["A"| ]  ["B"| ]  ["C"| ]  ["D"| ]  ["E"| null]
# first node is called "Head".

# in order creating the reference and passing it we will be using the "class".

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        new_node.next = self.head   # assigning the new nodes' next value of existing head
        self.head = new_node        #updating the head value, new node becomes the head
        
    def insert_at_middle(self,data,position):       # after any value
        new_node = Node(data)

        current_node = self.head

        if current_node:
            while current_node:
                if current_node.data == position:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                else:
                    current_node = current_node.next
            print("Position element not found")
        else:
            print("Position element not found")

    def insert_at_last(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        current_node = self.head

        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node

    def deletion_at_beginning(self):
        self.head = self.head.next

    def deletion_at_middle(self,value):
        current_node = self.head

        if current_node:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next


    def deletion_at_last(self):
        # if not empty
        current_node = self.head

        while current_node.next:
            if current_node.next.next == None:
                current_node.next = None
                return
            else:
                current_node = current_node.next
            


    
    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("None")

    def create_cycle(self):
        current_node=self.head

        while current_node:
            if current_node.next:
                current_node=current_node.next
            else:
                current_node.next=self.head
                return
            
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next    
            if slow == fast:
                print("cycle detected")  
                return        

        print("cycle is not detected")


li = Linked_list()
li.insert_at_last("A")
li.insert_at_middle(1,'A')
li.insert_at_last("B")
li.insert_at_last("C")
li.insert_at_begin(0)
li.deletion_at_beginning()
li.deletion_at_middle('B')
li.deletion_at_last()
li.create_cycle()
li.detect_cycle()

#print("LinkedList: ")
#li.print_List()


"""A clg maintains a list of student roll no using singly linked list , 
new student register throughout the day and their roll no's
must be added at the end of the list.Given a singly linked list and a 
new roll no insert the roll no at the end of the list nd return the updated list"""
# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at the end
def insert_at_end(head, roll_no):
    new_node = Node(roll_no)

    # If the list is empty
    if head is None:
        return new_node

    current = head
    while current.next:
        current = current.next

    current.next = new_node
    return head

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

head = None  # Empty list

# Insert roll numbers
head = insert_at_end(head, 101)
head = insert_at_end(head, 102)
head = insert_at_end(head, 103)

# Print updated list
print_list(head)



"""A bank uses a singly linked list to represent customers waiting in queue.
the manager wants to know how many customers are 
currently waiting.Given the head of a singly linked list
return the total no.of nodes in the list."""

# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to count number of customers (nodes)
def count_customers(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

# Creating linked list: 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Count customers
print("Total customers waiting:", count_customers(head))



# Linked list: A linked list is a linear data structure used to store a collection of elements (called nodes) where each node is connected to the next one using a link (pointer/reference).
# ["A"| ]  ["B"| ]  ["C"| ]  ["D"| ]  ["E"| null]
# first node is called "Head".

# in order creating the reference and passing it we will be using the "class".

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        new_node.next = self.head# assigning the new nodes' next value of existing head
        self.head = new_node        #updating the head value, new node becomes the head
        
    def insert_at_middle(self,data,position):       # after any value
        new_node = Node(data)

        current_node = self.head

        if current_node:
            while current_node:
                if current_node.data == position:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                else:
                    current_node = current_node.next
            print("Position element not found")
        else:
            print("Position element not found")

    def insert_at_last(self,data):
        new_node = Node(data)
        # if empty
        if self.head is None:
            self.head = new_node
            return
        
        # if not empty
        current_node = self.head

        while current_node.next:
            current_node=current_node.next
        current_node.next = new_node

    def deletion_at_beginning(self):
        self.head = self.head.next

    def deletion_at_middle(self,value):
        current_node = self.head

        if current_node:
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                else:
                    current_node = current_node.next


    def deletion_at_last(self):
        # if not empty
        current_node = self.head

        while current_node.next:
            if current_node.next.next == None:
                current_node.next = None
                return
            else:
                current_node = current_node.next
            


    
    def print_List(self):
        current_node = self.head
        while current_node:
            print(current_node.data ,end=" -> ")
            current_node = current_node.next
        print("None")

    def create_cycle(self):
        current_node=self.head

        while current_node:
            if current_node.next:
                current_node=current_node.next
            else:
                current_node.next=self.head
                return
            
    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next    
            if slow == fast:
                print("cycle detected")  
                return        

        print("cycle is not detected")


li = Linked_list()
li.insert_at_last("A")
li.insert_at_middle(1,'A')
li.insert_at_last("B")
li.insert_at_last("C")
li.insert_at_begin(0)
li.deletion_at_beginning()
li.deletion_at_middle('B')
li.deletion_at_last()
li.create_cycle()
li.detect_cycle()

#print("LinkedList: ")
#li.print_List()

