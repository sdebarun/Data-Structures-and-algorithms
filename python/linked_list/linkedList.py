
#! [ Author : Debarun Saha ]
#! [ Language : Python ]
#! [ Version : 3.8.9 ]

# ? Implementing linked list with python 
# ? The list is initially started with a value 
# ? using the constructor method. Later on shall
# ? be populated with diffrent methods
class myLinkedList :
    length = 0
    def __init__(self, value) -> None:
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head
        self.length = self.length + 1


    # Todo: adding elements to the end of the linekd list (at the tail)
    #* Time complexity = O(1)

    def append(self,value) -> dict :
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        # print(self.head)
        self.length += 1
        return self.head
        
    # Todo: adding elements at the begining of the linked list (at the head) 
    #* Time complexity = O(1)

    def prepend(self,value) -> dict :
        newNode = {
            "value" : value,
            "next"  : self.head
        }
        self.head = newNode
        self.length = self.length + 1
        return self.head
    
    # Todo: adding value at the provided index positonof the linked list
    #* Time complexity = O(n)

    def insert(self,index,value) -> dict :
        newNode = {
            "value" : value,
            "next" : None
        }
        prevNode = self.lookup(index-1)
        nextNode = prevNode['next']
        prevNode['next'] = newNode
        newNode['next'] = nextNode
        self.length += 1
        return self.head

    # Todo: Deleting a value from linked list [ O(n) ]
    #* Time complexity = O(n)

    def delete(self,value) -> dict :
        index = self.getIndex(value)
        deleteNode = self.lookup(index)
        prevNodeOfDeleteNode = self.lookup(index-1)
        nextNodeOfDeleteNode = deleteNode['next']
        prevNodeOfDeleteNode['next'] = nextNodeOfDeleteNode
        return self.head

    # Todo: Getting the positional index of a value of linked list 
    #* Time complexity = O(n)
    
    def getIndex(self,value) -> int :
        currentNode = self.head
        index = 0
        while currentNode != None : 
            # print(currentNode)
            if currentNode['value'] == value :
                return index
            currentNode = currentNode['next']    
            index += 1

    # Todo: Traversing through the linked list to find the node at the given index
    #* Time complexity = O(n)

    def lookup(self, index) -> dict :    
        counter = 0
        currentNode  = self.head
        while counter != index :
            currentNode = currentNode['next']
            counter += 1
        return currentNode

    # Todo: Printing the linked list as an array. In python it is list.
    #* Time complexity = O(n)

    def printList(self) -> list : 
        linkedList = list()
        currentNode = self.head
        while currentNode != None : 
            linkedList.append(currentNode['value'])
            currentNode = currentNode['next']
        print(linkedList)
        return


myLinkedList = myLinkedList(10)
myLinkedList.append(12)
myLinkedList.append(13)
# print(myLinekdList.viewList())
myLinkedList.prepend(1)

myLinkedList.printList()
# print(myLinkedList.length)

# myLinkedList.delete(12)
myLinkedList.printList()

# print(myLinkedList.lookup(2))

print(myLinkedList.insert(2,11))

myLinkedList.printList()

print(myLinkedList.delete(12))

myLinkedList.printList()


