
# impl binary tree and pre,in,post order
class BinaryTree():
    def __init__(self,Node):
        self.root=Node
        self.leftchild=None
        self.rightchild=None
    def insertLeft(self,newNode):
        if self.root is None:
            self.root=BinaryTree(newNode)
        elif self.leftchild is None:
            self.leftchild=BinaryTree(newNode)
        elif self.rightchild is None:
            self.rightchild=BinaryTree(newNode)
        else:
            self.leftchild.insertLeft(newNode)
    def preorder(self):
        if self is None:
            return None
        print(self.root)
        if self.leftchild is not None:
            self.leftchild.preorder()
        if self.rightchild is not None:
            self.rightchild.preorder()
    def inorder(self):
        if self is None:
            return None
        if self.leftchild is not None:
            self.leftchild.inorder()
        print(self.root)
        if self.rightchild is not None:
            self.rightchild.inorder()
    def postorder(self):
        if self is None:
            return None
        if self.leftchild is not None:
            self.leftchild.postorder()
        if self.rightchild is not None:
            self.rightchild.postorder()
        print(self.root)
    def breadth_travel(self):
        if self is None:
            return None
        quene=list()
        quene.append(self)
        while quene:
            node=quene.pop(0)
            print(node.root)
            if node.leftchild is not None:
                quene.append(node.leftchild)
            if node.rightchild is not None:
                quene.append(node.rightchild)

if __name__=='__main__':
    tree_one=BinaryTree('a')
    tree_one.insertLeft('b')
    test_list=['1','2','3','4']
    for i in test_list:
        tree_one.insertLeft(i)
    print("preorder")
    tree_one.preorder()
    print("inorder")
    tree_one.inorder()
    print("postorder")
    tree_one.postorder()
    print("breadth_travel")
    tree_one.breadth_travel()
        
  