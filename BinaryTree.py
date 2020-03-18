
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
        count=0
        while quene:
            node=quene.pop(0)
            print(node.root)
            count+=1
            if node.leftchild is not None:
                quene.append(node.leftchild)
            if node.rightchild is not None:
                quene.append(node.rightchild)
        print(count)
    def depth_node(self,node):
        if node is None:
            return 0
        d1=self.depth_node(node.leftchild)
        d2=self.depth_node(node.rightchild)
        return max(d1,d2)+1
    def preorder_bypostandin(self,inorder_list,postorder_list):
        if not postorder_list:
            return None
        print(inorder_list)
        print(postorder_list)
        root=BinaryTree(postorder_list[-1])
        print(postorder_list[-1])
        in_root_index=inorder_list.index(postorder_list[-1])
        root.leftchild=self.preorder_bypostandin(inorder_list[0:in_root_index],postorder_list[0:in_root_index])
        root.rightchild=self.preorder_bypostandin(inorder_list[in_root_index+1:],postorder_list[in_root_index:-1])
        #print(root)
        return root
    def postorder_bypreandin(self,inorder_list,preorder_list):
        if not preorder_list:
            return None
        print(inorder_list)
        print(preorder_list)
        root=BinaryTree(preorder_list[0])
        print(preorder_list[0])
        in_root_index=inorder_list.index(preorder_list[0])
        root.leftchild=self.postorder_bypreandin(inorder_list[0:in_root_index],preorder_list[1:in_root_index+1])
        root.rightchild=self.postorder_bypreandin(inorder_list[in_root_index+1:],preorder_list[in_root_index+1:])
        #print(root)
        return root
    def preorder_two(self):
        if self is None:
            return None
        print(self.root,end=" ")   #输出不换行
        if self.leftchild is not None:
            self.leftchild.preorder_two()
        if self.rightchild is not None:
            self.rightchild.preorder_two()
        



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
    print("depth_node")
    max_depth=tree_one.depth_node(tree_one)
    print(max_depth)
    print("preorder_bypostandin")
    inorder_list_demo=['4','2','b','3','a','1']
    postorder_list_demo=['4','2','3','b','1','a']
    root_all_nodes=tree_one.preorder_bypostandin(inorder_list_demo,postorder_list_demo)
    print("preorder all nodes")
    root_all_nodes.preorder_two()
    print("postorder_bypreandin")
    inorder_list_demo=['4','2','b','3','a','1']
    preorder_list_demo=['a','b','2','4','3','1']
    root_all_nodes=tree_one.postorder_bypreandin(inorder_list_demo,preorder_list_demo)
    print("postorder all nodes")
    root_all_nodes.postorder()
    
    
  