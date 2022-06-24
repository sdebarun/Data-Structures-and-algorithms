class myLinekdList:
    def __init__(self, value) -> None:
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head

    def append(self,value) :
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        # print(self.head)
        return self.head
        
    
    def prepend(self,value) :
        newNode = {
            "value" : value,
            "next"  : self.head
        }
        self.head = newNode

        return self.head



myLinkedList = myLinekdList(10)
print(myLinkedList.append(12))
print(myLinkedList.append(13))
# print(myLinekdList.viewList())
print(myLinkedList.prepend(1))