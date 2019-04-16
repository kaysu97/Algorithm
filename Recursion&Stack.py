#!/usr/bin/env python
# coding: utf-8

# f()的複雜度是多少
def f(problemSize):
	work = 0
	for i in range(problemSize):
		for j in range(i, problemSize):
			work += 1


class Solution01:
    def complexity(self):
         print("n^2") # print your answer here.


# 把所有位數相加用Recursion的方式
class Solution02:
    def addDigits(self, num):
      
        if num < 10:
            return num
            
        else:
            num = num % 10 + self.addDigits(int((num)/10))
            if (num >=10):
                return self.addDigits(num)
            else:
                return (num)
        
        
       


# In[8]:


s = Solution02()
s.addDigits(258)


# In[3]:


class Solution02_Re:
    def addDigits(self, num):
        return (num%9)


s = Solution02_Re()
s.addDigits(258)


#找出palindrome的單字，palindrome是一種正的寫跟反過來寫是一樣的單字，例如:madam
class Solution04:
    def isPalindrome(self, s):
        s = ''.join(c for c in s if c.isalpha())
        if s==s[::-1]:
            return True
        else:
            return False
    



s = Solution04()
print(s.isPalindrome("never odd or even"))
print(s.isPalindrome("madam"))
print(s.isPalindrome("mad"))


#用Stack的方式找出palindrome的單字
class Stack:
    
    # variables 
    # __size__ = 0 # another way to implement size()
    items = None
    
    # functions
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
        
    def push(self, item):
        self.items.append(item) # The method append() appends a passed obj into the existing list.

    def pop(self):
        return self.items.pop() # The method pop() removes and returns last object or obj from the list.
    
    def peek(self):
        return self.items[len(self.items)-1]
    


# In[234]:
class Solution04_stack:
    def isPalindrome(self,s):
        st=Stack()
        for c in s :
            if c.isalpha():
                st.push(c)
            
        for c in st.items:
            if c != st.pop():
                return False
                break
        else:
            return True


# In[235]:


s=Solution04_stack()
print(s.isPalindrome("never odd or even"))
print(s.isPalindrome("madam"))
print(s.isPalindrome("mad"))

