#!/usr/bin/env python
# coding: utf-8

# Build the Huffman tree for the set of characters in this question. Include all characters. How many bits are saved in the storage of this question using Huffman trees versus a storage based on a fixed-length encoding?
class Huffman:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val
    def print_tree(self,data,a):
        
        if self.left:
            self.left.print_tree(data+"0",a)
        if self.val[1]:
            a.append(self.val[0]*7-len(data)*self.val[0])
#             print(self.val[0],"",self.val[1])
        if self.right:
            self.right.print_tree(data+"1",a)
    

class Solution_H05_P01:
    li=[]
    lich=[]
    litree=[]
    def answer(self,st):
        for  i in range(len(st)):
            
            if st[i] in self.lich:
                pass
            else:
                self.li.append([st.count(st[i], i,len(st)),st[i]])
                self.lich.append(st[i])
        self.li=sorted(self.li,key=lambda p:p[0])
        for i in range(len(self.li)):
            self.litree.append(Huffman(None,None,self.li[i]))
        while len(self.litree)>1:
            self.litree.append(Huffman(self.litree[0],self.litree[1],[self.litree[0].val[0]+self.litree[1].val[0],None]))
            self.litree.pop(0)
            self.litree.pop(0)
            self.litree=sorted(self.litree,key=lambda p:p.val[0])
        a=[]
        self.litree[0].print_tree("",a)
        
        print(sum(a))
        
                
                


s=Solution_H05_P01()
st="Build the Huffman tree for the set of characters in this question. Include all characters. How many bits are saved in the storage of this question using Huffman trees versus a storage based on a fixed-length encoding?"

s.answer(st)



#Construct the next table for the following string aabbaabababbaabbaabb.
class Solution_H05_P02:
    def answer(self):
        print(self.compute_next('aabbaabababbaabbaabb'))
    def compute_next(self,B):
        next_ = [0] * len(B)
        next_[0] = -1
        next_[1] = 0

        for i in range(2, len(B)):
            j = next_[i-1] 
            while B[i-1] != B[j] and j >= 0:
                j = next_[j]

            if j == next_[i-1]:
                next_[i] = next_[i-1] + 1
            elif j == -1: 
                next_[i] = 0
            elif j == 0: 
                next_[i] = 0
            else: 
                next_[i] = j + 1

        return next_

s=Solution_H05_P02()
s.answer()


#Modify the KMP string matching algorithm to find the largest prefix of B that matches a substring of A. In other words, you do not need to match all of B inside A, instead, you want to find the largest match (but it has to start with b1).
class Solution_H05_P03:
    def compute_next(self,B):
        next_ = [0] * len(B)
        next_[0] = -1
        next_[1] = 0

        for i in range(2, len(B)):
            j = next_[i-1] 
            while B[i-1] != B[j] and j >= 0:
                j = next_[j]

            if j == next_[i-1]:
                next_[i] = next_[i-1] + 1
            elif j == -1: 
                next_[i] = 0
            elif j == 0: 
                next_[i] = 0
            else: 
                next_[i] = j + 1

        return next_
    def find_the_largest_prefix(self, A, B):
        
        _next = self.compute_next(B)
        ma=0
        n = len(A)
        m = len(B)

        i = 0 
        j = 0 

        while i < n: 
            if B[j] == A[i]:
                j += 1
                i += 1
            else: 
                if j >=ma:
                    ma=j
                if _next[j] == -1: 
                    i += 1
                elif _next[j] == 0: 
                    j = 0
                else: 
                    j = _next[j] 

#

        return B[:ma]


# In[85]:


A="xyxyxyxyxyxyyyyyxyxyx"
B="xyyxxxyy"
s=Solution_H05_P03()
print(s.find_the_largest_prefix(A, B))


#You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
class TreeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x
    def printt(self):
        print(self.val)
        if(self.left):
            self.left.printt()
        elif(self.right):
            self.right.printt()
class Solution_H05_P04:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans



n1=TreeNode(1)
n1.left=TreeNode(3)
n1.left.left=TreeNode(5)
n2=TreeNode(2)
n2.left=TreeNode(9)
n1.printt()
n2.printt()
s=Solution_H05_P04()
s.mergeTrees(n1,n2).printt()


#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
#Solve the problemby using dynamic programming.
class Solution_H05_P05:

    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)



s=Solution_H05_P05()
s.climbStairs(3)


# In[ ]:




