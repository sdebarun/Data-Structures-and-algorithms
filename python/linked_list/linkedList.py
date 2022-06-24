
#! [ Author : Debarun Saha ]
#! [ Language - Python ]
#! [ Version : 3.8.9 ]
#! [ Date : 24-06-2022 ]

# Todo : custom linked list implementation in python
# Todo : append  and prepend  has O(1)
# Todo : insert will have O(n) - yet to be impleneted
# Todo : delete will have O(n) - yet to be impleneted
# Todo : The list will start with one node having value 10
class myLinkedList:
    length = 0
    def __init__(self, value) -> None:
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head
        self.length = self.length + 1

    def append(self,value) :
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        # print(self.head)
        self.length += 1
        return self.head
        
    
    def prepend(self,value) :
        newNode = {
            "value" : value,
            "next"  : self.head
        }
        self.head = newNode
        self.length = self.length + 1
        return self.head

    def printList(self) : 
        linkedList = list()
        currentNode = self.head
        while currentNode != None : 
            # print(currentNode)
            linkedList.append(currentNode['value'])
            currentNode = currentNode['next']
        print(linkedList)
        return
    
    def delete(self,value) :
        index = self.getIndex(value)
        deleteNode = self.lookup(index)
        prevNodeOfDeleteNode = self.lookup(index-1)
        nextNode = deleteNode['next']
        prevNodeOfDeleteNode['next'] = nextNode
        return self.head


    def insert(self,index,value) :
        currentNode = self.head
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

    def getIndex(self,value) :
        currentNode = self.head
        index = 0
        while currentNode != None : 
            # print(currentNode)
            if currentNode['value'] == value :
                return index
            currentNode = currentNode['next']    
            index += 1

    def lookup(self, index) :    
        counter = 0
        currentNode  = self.head
        while counter != index :
            currentNode = currentNode['next']
            counter += 1
        return currentNode



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


