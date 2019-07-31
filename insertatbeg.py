# class node to store data and next
class Node:

  def __init__(self,data, next=None):
    self.data = data
    self.next = next
  
  # defining getter and setter for data and next
  def getData(self):
    return self.data
  
  def setData(self, data):
    self.data = data
  
  def getNextNode(self):
    return self.next
  
  def setNextNode(self, node):
    self.next = node

# class Linked List
class LinkedList:

  def __init__(self, head=None):
    self.head = head
    self.size = 0

  def addNode(self, data):
    node = Node(data, self.head)
    self.head = node
    # incrementing the size of the linked list
    self.size += 1
    return True

  #method to insert at the beginning of the linked list
  def insert_at_beginning(self,data):
    new_node= Node(data,self.head)
    new_node.setData(data)

    if self.size ==0:
      self.head = new_node
      return True

    else:
      new_node.setNextNode(self.head)
      self.head = new_node
      return True

    self.size +=1
  
 
  # print the linked list
  def printLL(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.getNextNode()
      
           
myList = LinkedList()
print(myList.addNode(25))
print(myList.addNode(78))
print(myList.addNode(32))
print(myList.insert_at_beginning(30))

myList.printLL()


