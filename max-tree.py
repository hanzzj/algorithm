class treenode:
    def __init__(self, attr, left = None, right = None):
        self.attr = attr
        self.left = left
        self.right = right
        
def create_tree(list1):
    if len(list1)==0:
        return None
    if len(list1)==1:
        node = treenode(list1[0])
        return node
    root = max(list1)
    node = treenode(root)
    i = list1.index(root)
    if i>0:
        #print(list1[0:i])
        node.left = create_tree(list1[0:i])
    if i<(len(list1)-1):
        #print(list1[i+1:])
        node.right = create_tree(list1[i+1:])
    return node

def print_tree(treenode):
    print("节点"+str(treenode.attr))
    if treenode.right != None:
        print("右孩子节点;"+str(treenode.right.attr))
    if treenode.left != None:
        print("左孩子节点;"+str(treenode.left.attr))
    if treenode.right != None:
        print_tree(treenode.right)
    if treenode.left != None:
        print_tree(treenode.left)

node = create_tree([3,2,1,6,0,5])
print_tree(node)
