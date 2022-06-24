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



myLinkedList = myLinekdList(10)
print(myLinkedList.append(12))
print(myLinkedList.append(13))
# print(myLinekdList.viewList())
print(myLinkedList.prepend(1))

print(myLinkedList.length)