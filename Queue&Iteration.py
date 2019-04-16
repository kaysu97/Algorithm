
# coding: utf-8

# In[1]:


class Queue:
    
   
    items = None
    
    # functions
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
   
   
    
        


# In[27]:


class Solution:
    def dailyTemperatures(self,temperatures):
        for t in range(len(temperatures)):
            for h in range(t+1,len(temperatures)):
                if temperatures[t]<temperatures[h] and t!=len(temperatures)-1 :
                    temperatures[t] = h-t
                    break
            else :
                temperatures[t] = 0
                
        return temperatures
                
        
        


# In[31]:


s = Solution()
te=[73, 74, 75, 71, 69, 72, 76, 73]

print(s.dailyTemperatures(te))

