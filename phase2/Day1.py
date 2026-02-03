#two polynomial addtion using linked list
"""class node:
    def __init__(self,c,p):
        self.c=c
        self.p=p
        self.next=None
def create_polynomial(terms):
    head=tail=None
    for i in range(terms):
#adding 2 polynomials using linked list
class Node:
  def __init__(self,data,power):
    self.data=data
    self.power=power
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def insert_at_begin(self,data,power):
    new_node=Node(data,power)
    new_node.next=self.head
    self.head=new_node
  def insert_at_end(self,data,power):
    new_node=Node(data,power)
    if self.head==None:
      self.head=new_node
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=new_node
  def print_list(self):
    temp=self.head
    while temp:
      print(temp.data,"x^",temp.power,"+",end=" ")
      temp=temp.next
  print(None)
ll=Linkedlist()
ll.insert_at_begin(9,2)
ll.insert_at_end(4,1)
ll.print_list()"""
#vaild parenthesis
def vaild(s):
    stack=[]
    pairs={")":"(","]":"[","}":"{","@":"@"}
    for char in s:
        if char in pairs:
            if len(stack)== 0 or stack[-1]!=pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack)==0

s1=input()
print(vaild(s1))








