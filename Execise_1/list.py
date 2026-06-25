'''#List Exercises
#1: Perform Basic List Operations
n=[1,2,3,4,5,6]
print(n)

#2: Perform List Manipulation
n=list(map(int,input("enter the list of numbers:").split()))
n.insert(3,10)
print(n)



#3: Sum and average of all numbers in a list
n=list(map(int,input("enter the list of numbers:").split()))
p=len(n)
print(p)
c=0
for x in n:
    c=x+c
print(f"sum ot the list is {c}")
print(f"average of the sum of the list is {c//p}")


#4: Reverse a list
n=list(map(int,input("enter the list of numbers:").split()))
n.reverse()
print(n)       

#5: Turn every item of a list into its square
n=[1,2,3,4,5,6,]
l=list(map(lambda a:a**2,n))
print(l)         

 
#6: Find Maximum and Minimum
n=[2,4,6,8,10,12,14,16]
print(f"maximum number {max(n)}, &  minimum number {min(n)}")          


#7: Count Occurrences
n=[2,4,6,8,10,12,4,6,14,1,6,16,1,2,3,4,5,6,18,20]
print(n.count(6))                  


#8: Sort a list of numbers
n=[2,4,6,8,10,12,4,6,14,1,6,16,1,2,3,4,5,6,18,20]
n.sort()
print(n)  

#9: Create a copy of a list
l=list(map(int,input("enter the list of the numbers:").split()))
k=l.copy()
print(k)      


#10: Combine two lists
l1=[1,2,3]
l2=[4,5,6]
#l1=l1+l2
l1.extend(l2)
print(l1)       


#11: Remove empty strings from the list of strings
#l=list(map(str,input("enter the list of strings").split()))
l=['hari','ravi','giri',' ', ' ']
k=[]
for x in l[:]:
    if x == ' ':
        l.remove(x)
print(l)    


#12: Remove Duplicates from list
l=['hari','ravi','giri',' ', ' ','giri']
k=set(l)
l=list(k)
print(l)        


#13: Remove all occurrences of a specific item from a list
n=[2,4,6,8,10,12,4,6,14,1,6,16,1,2,3,4,5,6,18,20]
p=int(input("Enter the numberto remove:"))
for x in n:
    if x==p:
        n.remove(x)
print(n)        


#14: List Comprehension for Numbers
nums = [1, 2, 3, 4]
n = [x for x in nums if x % 2 == 0]
print(n)       


#15: Access Nested Lists
l=[[1,2],[3,4],[5,6]]
for i in l:
    for x in i:
        print(x)    


l= [1,2, [3,4,[5,6,[7,8], 9],10],11]
def flat_list(l):
    nl = []
    for i in l:
        if isinstance(i, list):
            nl.extend(flat_list(i))
        else:
            nl.append(i)
    return nl
print(flat_list(l))        


#17: Concatenate two lists index-wise
l1=["1","2","3"]
l2=["4","5","6"]
for x,y in zip(l1,l2):
    print(x+y)        


#18: Concatenate two lists in the following order
list1 = ["Hello ", "Take "]
list2 = ["Dear", "Sir"]
for x, y in zip(list1, list2):
    print(x + y)


#19: Iterate both lists simultaneously
l1=[1,2,3]
l2=[4,5,6,7]
for x,y in zip(l1,l2):
    print(x,y)            


#21:Add new item to list after a specified item
l=[1,2,3,4,5,6,7,]
s=int(input("enetr the index to add item"))
p=l.index(s)
l2=[4,5,6]
for i in l2:
    l.insert(p+1,i)
print(l)           



#22: Extend nested list by adding the sublist
l=[[1,2],[3,4],[5,6]]
k=['a','b']
l.extend(k)
print(l)    '''


#23: Replace list’s item with new value if found
l1=[1,2,3,4,5]
res=[]
replace1=3
for i in l1:
     if i==replace1:
         res.append(10)
     else:
         res.append(i)
       
print(res)

