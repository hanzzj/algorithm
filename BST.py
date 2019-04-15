# -*- coding:utf-8 -*-
#由输入数组构二叉搜索树
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
            
#找出最小距离
class find_min:
   def minDist(self, root):
        if root == None:
            return 0
        else:
            res = []
            self.middle(root, res)
        if len(res) == 1:
            return res[0]
        min_dist = res[1]-res[0]
        for i in range(2,len(res)):
            if res[i]-res[i-1] < min_dist:
                min_dist = res[i]-res[i-1]
        return min_dist
 
   def middle(self,root,res):
        if root == None:
            return
        self.middle(root.left,res)
        res.append(root.data)
        self.middle(root.right,res)

root =[4,2,6,1,3,None,None]
treeroot=TreeNode(root[0])
s=find_min()
i=1
while i <len(root):
     if(root[i])!=None:
        treeroot.insert(root[i])
     i+=1
print("最小距离为:",s.minDist(treeroot))

