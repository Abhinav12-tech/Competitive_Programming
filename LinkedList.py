class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
    
   def AtBegining(self,newdata):
      NewNode = Node(newdata)

    # Update the new nodes next val to existing node
      NewNode.nextval = self.headval
      self.headval = NewNode
      
   def AtEnd(self, newdata):
      NewNode = Node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode
      
   def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode
      
   def RemoveNode(self, Removekey):
      headval = self.headval
         
      if (headval is not None):
         if (headval.dataval == Removekey):
            self.head = headval.nextval
            headval = None
            return
      while (headval is not None):
         if headval.dataval == Removekey:
            break
         prev = headval
         headval = headval.nextval

      if (headval == None):
         return

      prev.nextval = headval.nextval
      headval = None

list = SLinkedList()
list.headval = Node("Competitive")
e2 = Node("Programming")
e3 = Node("Lab")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
#print("\n")

print("Inserting Element at Start of Linked List :-")
list.AtBegining("2 Hours")
list.listprint()

print("\nInserting Element at End of Linked List :-")
list.AtEnd("Today")
list.listprint()

print("\nInserting Element in between of Linked List :-")
list.Inbetween(list.headval.nextval,"(Semester5)")
list.listprint()

print("\nDeleting Element in Linked List :-")
list.RemoveNode("(Semester5)")
list.listprint()
