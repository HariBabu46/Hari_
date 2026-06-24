'''#1: Perform Basic Tuple Operations
t=(1,2,3,4,5,6)
t2=(8,9,10)
t=t+t2
print(t)


#2: Tuple Repetition
t=(1,2,3,4,)
print(t*2)

#3: Slicing Tuples
t=(1,2,3,4,5,6,7,8,9)
print(t[1:9])


#4: Reverse the tuple
t=(1,2,3,4,5,6,7,8,9)
print(t[::-1])

#5: Access Nested Tuples
t=((1,2),(3,4),(5,6))
print(t[1][0])

#6: Create a tuple with single item 50
t=(50,)
print(t)


#7: Unpack the tuple into 4 variables
t = (10, 20, 30, 40)
a, b, c, d = t
print(a)
print(b)
print(c)
print(d)


#8: Swap two tuples in Python
t1=(1,2,3,4)
t2=(5,6,7,8)
t1,t2=t2,t1
print(t1,t2)


#9: Copy Specific Elements From Tuple
t=(1,2,3,4,5,6,7,8,9)
k=t[4]
print(k)


#10: List to Tuple
l=[1,2,3,4,5,6,7,8,9]
t=tuple(l)
print(t)

#11: Function Returning Tuple
def multiply(t):
    return t*2
t=tuple(map(int,input("enter the numbers").split()))
print(t)
p=multiply(t)
print(p)


#12: Comparing Tuples
t1=(1,2,3,4)
t2=(5,6,7,8)
for x,y in zip(t1,t2):
    if x>y:
        print(x,"is greater")
    else:
        print(y ," is greater")


#13: Removing Duplicates from Tuple
t=(1,2,3,4,5,6,3,4,2,6,4,8,7,8,9)
s=set(t)
t=tuple(s)
print(t)


#14: Filter Tuples
t=(1,2,3,4,5,6,7,8,9)
p=tuple(filter(lambda x:x%2==0, t))
print(p)

#15: Map Tuples
t=(1,2,3,4,5,6,7,8,9)
p=tuple(map(lambda x:x*x,t))
print(p) '''

#16: Modify Tuple
t=(1,1,1,1,0,1,1,1)
t=list(t)
t.pop(4)
t=tuple(t)
print(t)


#17: Sort a tuple of tuples by 2nd item
t = ((1, 5), (2, 3), (3, 1), (4, 4))
p = tuple(sorted(t, key=lambda x: x[1]))
print(p)


#18: Count Elements
t=(1,2,3,4,5,6,7,8,9)
print(len(t))


#19: Check if all items in the tuple are the 
t=(1,1,1,1,0,1,1,1)
k=t[0]
c=0
for x in t:
    if x==k:
         c=c+1
if c==len(t):
        print("same")
else:
        print("not same")
    
