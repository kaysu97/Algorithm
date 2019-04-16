
# coding: utf-8

# 用Bubble sort、selection sort 、insertion sort的方式並算出swap()的次數
class Solution01:
   
    def swap(self,li,i,j): 
        
        tmp = li[i]
        li[i] = li[j]
        li[j] = tmp
        
    def bubbleT(self,li):
        bcount=0
        for i in range(len(li)):
            for j in range(i):
                if li[i] < li[j]: 
                    self.swap(li,i,j)
                    bcount = bcount+1
        return bcount
    
    def selectionT(self, li):
        i = 0 
        scount = 0
        while i < len(li): 
            j = i
            minIndex = j 
            while j < len (li): 
                if li[j] < li[minIndex]: 
                    minIndex = j
                j += 1
            self.swap(li, minIndex, i)
            i += 1
            scount=scount+1
        return scount
    
    def insertionT(self, li):
        icount = 0
        for sortedIndex in range(1, len(li) - 1):
            targetIndex = sortedIndex + 1
            for i in range(0, sortedIndex + 1):
                if li[targetIndex] > li[i]: 
                    pass
                else:
                    self.swap(li, i, targetIndex)
                    icount=icount+1
        return icount
    
rli = list(range(999, -1, -1))
s = Solution01()
print(s.bubbleT(rli))
rli = list(range(999, -1, -1))
print(s.selectionT(rli))
rli = list(range(999, -1, -1))
print(s.insertionT(rli))


# In[114]:


rli = list(range(999, -1, -1))
s = Solution01()

print(s.bubbleT(rli))
print(s.selectionT(rli))
print(s.insertionT(rli))

s=Solution01()
rli = list(range(999, -1, -1))
print(s.bubbleT(rli))
rli = list(range(999, -1, -1))
print(s.selectionT(rli))
rli = list(range(999, -1, -1))
print(s.insertionT(rli))


# 為何insertion sort 的次數比selection sort的次數少?
class Solution02:
    def why(self):
        print("因為insertion sort每一次都會重複排，每次都是新的數列，隨著目標數字移動，它前面的所有數字都要和它比較，但是如果數列已由小到大排好，那就完全不會交換，但此題為由大到小所以交換次數為接近n^2；而selection sort是不管數字多大，且排序如何，就算你是已經由小到大排好了，還是會排n次，因為每輪都會找此次的最小值，排序次數是固定的。此題為由大到小排，所以selection sort交換次數會比insertion sort還少。")


# In[38]:


s = Solution02()
s.why()


# 給一個由小到大排好的數列，若今天要插入一個數字，請用二元樹的方式插入此數字到數列中
class Solution03:
    def searchInsert(self, nums, target):
        left = 0 
        right = len(li) - 1 

        while left <= right:     
            mid = (left + right) // 2

            if target == li[mid]:
                return mid
            elif target < li[mid]:
                right = mid - 1
            else: 
                left = mid + 1

   
        return left


# In[107]:


s=Solution03()
li=[2,4,6,8,9,35,48]
print(s.searchInsert(li,35))
li=[2,4,6,8,9,48]
print(s.searchInsert(li,35))


# 找出數列中只出現一次的數字
class Solution04:
    def singleNonDuplicate (self, nums):
        left = 0 
        right = len(nums) 
        
        while True:     
            even = list(range( left , right, 2))
            evenmid = (len(even)-1) // 2 
            
            mid = even[evenmid]

            if nums[mid] == nums[mid+1]:
                left =  mid+2 
                if left >= len(nums)-1:
                    return nums[left]
            elif nums[mid] == nums[mid-1]:
                right = mid - 1
                if right <= 0:
                    return nums[right]
            else : 
                return nums[mid]
            
                break
              

        
        


# In[40]:


li=[1,1,2,2,3,3,4,4,10,10,540,1000,1000]
s=Solution04()
print(s.singleNonDuplicate(li))

ri=[1,1,2,2,3,3,4,4,10,10,540]
s=Solution04()
print(s.singleNonDuplicate(ri))

ri=[1,1,2,2,3,4,4,10,10]
s=Solution04()
print(s.singleNonDuplicate(ri))

ri=[1,1,2,2,3,3,4,10,10]
s=Solution04()
print(s.singleNonDuplicate(ri))

ri=[1,2,2,3,4,4,10,10]
s=Solution04()
print(s.singleNonDuplicate(ri))
        

