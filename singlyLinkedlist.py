#Type declaration for singly linked list of integers

class Node:
	#constructor
	def __init__(self):
		self.data = None
		self.next = None
	#method for setting the data field
	def set_data(self,data):
		self.data= data

	#method for getting the data field
	def get_data(self):
		return self.data

	#method for setting the next field 
	def set_next(self,next):
		self.next = next

	#method for getting next field of the data
	def get_next(self):
		return self.next

	#returns true if node points to another node
	def has_next(self):
		return self.next!=None

#method to traverse the linked list
def traverse(self):
        node = self # start from the head node
        while node != None:
            print(node.data )# access the node value
            node = node.next # move on to the next node
	
head=Node()
head.set_data(21)
node2=Node()
node2.set_data(42)
node3=Node()
node3.set_data(1)
head.set_next(node2)
node2.set_next(node3)

#passing the head node as parameter to traverse function
traverse(head)