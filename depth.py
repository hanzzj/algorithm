# -*- coding:utf-8 -*-
#二叉树节点定义
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
    def insert(self,x):
        if x<self.data:
          if self.left:
            self.left.insert(x)
          else:
            tree=TreeNode(x)
            self.left=tree
        elif x>self.data :
          if self.right:
            self.right.insert(x)
          else:
            tree=TreeNode(x)
            
#两种方法找出最小深度
class find_min:
   def DFS_minDepth(self, root):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        elif root.left == None and root.right != None:
            return self.DFS_minDepth(root.right)+1
        elif root.right ==None and root.left != None:
            return self.DFS_minDepth(root.left)+1
        elif root.left != None and root.right !=None:
            return min(self.DFS_minDepth(root.left), self.DFS_minDepth(root.right))+1
 
   def BFS_minDepth(self,root):
        if not root:
            return 0
        curLevelNodeList = [root]
        minLen = 1
        while curLevelNodeList is not []:
            tempNodeList = []
            for node in curLevelNodeList:
                if not node.left and not node.right:
                    return minLen
                if node.left is not None:
                    tempNodeList.append(node.left)
                if node.right is not None:
                    tempNodeList.append(node.right)
            curLevelNodeList = tempNodeList
            minLen += 1
        return minLen

root, nodes =[3,9,20,None,None,15,7], []
i,j=0,0
for i in range(len(root)):
    nodes.append(TreeNode(root[i]))
while j<len(root):
    if 2*(j+1)<len(root):nodes[j].left = nodes[2*(j+1)]
    else:nodes[j].left = None
    if (2*(j+1)+1)<len(root):nodes[j].right=nodes[2*(j+1)+1]
    else:nodes[j].right = None
    j+=1
s=find_min()
print("最小深度:DFS:",s.DFS_minDepth(nodes[0]),"  BFS:",s.BFS_minDepth(nodes[0]))
