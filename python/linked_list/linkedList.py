from hashlib import new


class myLinekdList:
    def __init__(self, value) -> None:
        self.head = {
            "value" : value,
            "next" : None
        }
        self.tail = self.head
        # print(self.head)

    # def viewList(self):
    #     return self

    def append(self,value) :
        new_node = {
            "value" : value,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        print(self.head)
        # return self
    


myLinkedList = myLinekdList(10)
print(myLinkedList.append(12))
print(myLinkedList.append(13))
# print(myLinekdList.viewList())