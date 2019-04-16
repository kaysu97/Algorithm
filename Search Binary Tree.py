
# coding: utf-8

# Implement a binary search tree by using a single list (an example is shown as follow).
#Insert the following new items: 4, 2, 1, 3, 6, 5 into the binary search tree, and print the tree nodes in inorder.
class Solution_H04_P01:
    
    list=[1,2,3,4,5,6]
    print(list)
    


#Print the tree nodes in Q1 in postorder.
class Solution_H04_P02:
    
    
    list=[1,3,2,5,6,4]
    print(list)


# Algorithm insert() of the binary minheap may swap elements many times up the heap.
#Modify the algorithm so that at most one swap will be performed. (Note that O(logn) comparisons are still allowed.)
class Solution_H04_P03:
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    
    def insert_new(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        j = self.currentSize
        while k < self.heapList[j // 2]:
            self.heapList[j]=self.heapList[j // 2]
            j = j//2
        
        else:
            self.heapList[j]=k

h = Solution_H04_P03()

items = [11, 9,5 , 18, 8, 19, 21, 33, 17, 27]
for i in items:
    h.insert_new(i)
print(h.heapList)
            


#return the minimum difference between the values of any two different nodes in the tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution_H04_P04:
    li=[]
    def print_tree(self,root):
        
        if root.left:
            self.print_tree(root.left)
        self.li.append(root.val)
        if root.right:
            self.print_tree(root.right)

    
    def minDiffInBST(self,root):

        d=float("inf")
        self.print_tree(root)
        for i in range(len(self.li)-1,0,-1):
            a=self.li[i]-self.li[i-1]
            if a<d:
                d=a
        return d
            
        
        


# In[70]:


r=TreeNode(4)
r.left=TreeNode(2)
r.right=TreeNode(6)
r.left.left=TreeNode(1)
r.left.right=TreeNode(3)

s=Solution_H04_P04()

# s.minDiffInBST(r)
# s.minDiffInBST(6)
# s.minDiffInBST(1)
# s.minDiffInBST(3)

print(s.minDiffInBST(r))

