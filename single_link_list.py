class Node(object):
    # 节点
    #__init__构造函数
    def __init__(self,elem):
        #elem 存放数据，next是下一个节点的标识
        self.elem = elem
        self.next1 = None

class SingleLinkList(object):
    def __init__(self,node=None):
        self.__head = node
    def is_empty(self):
        #是否为空
        return self.__head == None
    def length(self):
        #cur用来遍历节点
        cur = self.__head
        count = 0
        while cur !=None:
            count +=1
            cur = cur.next1
        return count
    def travel(self):
        cur = self.__head
        while cur !=None:
            print(cur.elem,end=" ")
            cur = cur.next1
        print("")

    def add(self,item):
        # 链表头部添加元素
        node = Node(item)
        node.next1 = self.__head
        self.__head = node

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head=node
        else:
            cur = self.__head
            while cur.next1 != None:
                cur = cur.next1
            cur.next1 = node

    def remove(self,item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next1
                else:
                    pre.next1 = cur.next1
            else:
                pre = cur
                cur = cur.next1

if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.travel()