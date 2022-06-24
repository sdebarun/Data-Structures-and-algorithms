
# Todo : custom linked list implementation in python
# Todo : append  and prepend  has O(1)
# Todo : insert will have O(n) - yet to be impleneted
# Todo : delete will have O(n) - yet to be impleneted
# Todo : The list will start with one node having value 10

class myLinekdList:
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
        linkedList = []
        currentNode = self.head
        while currentNode != None : 
            # print(currentNode)
            linkedList.append(currentNode['value'])
            currentNode = currentNode['next']
        return linkedList
    
    def delete(value) :
        pass


myLinkedList = myLinekdList(10)
myLinkedList.append(12)
myLinkedList.append(13)
# print(myLinekdList.viewList())
myLinkedList.prepend(1)

#! printing out the linked list and its length
#! printing the linked list in 
print(myLinkedList.printList())
print(myLinkedList.length)
