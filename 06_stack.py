
class Stack(object):
    def __init__(self):
        self.__list=[]
    def push(self,item):
        self.__list.append(item)
    def pop(self):
        return self.__list.pop()

    def is_empty(self):
        '''判断是否为空'''

        return self.__list==[]

    def size(self):
        return len(self.__list)

if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())