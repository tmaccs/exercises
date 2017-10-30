class Node(object):
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue != None:
            cur_node = queue.pop(0)
            if cur_node.lchild == None:
                cur_node.lchild = node
                #执行完之后就可以退出了
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def broadth_travel(self):
        # 广度遍历
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.broadth_travel()