'''# 1: Perform basic dictionary operations
d={1:"one",2:"two",3:"three",4:"four"}
print(d)


#2: Perform dictionary operations
d={1:"one",2:"two",3:"three",4:"four"}
for x,y in d.items():
    print(x,y)

#3: Dictionary from Lists
l1=[1,2,3,4,5]
l2=["one","two","three","four","five"] 
d=dict(zip(l1,l2))
print(d)


#4: Clear Dictionary
d={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
d.clear()
print(d)   


#5: Merge two Python dictionaries into one
d1={'a':"apple",'b':"banana",'c':"carrot"}
d2={'d':"dragonfruit",'k':"kiwi"}
d1.update(d2)
print(d1)         

#6: Count Character Frequencies
s=input("enter the string:")
d={}
for i in s:
    if i  in d:
        d[i]+=1
    else:
        d[i]=1
print(d)                 


# 7: Access Nested Dictionary
d1={'a':"apple",
    'b':"banana",
    'n':{1: "one", 2: "two", 3: "three"},
    'c':"carrot"}
print(d1['n'][1])           


#8: Print the value of key ‘history’ from nested dict
student = {
    "name": "Hari",
    "marks": {
        "maths": 90,
        "science": 85,
        "history": 88
    }
}
print(student["marks"]["history"])



#9: Modify Nested Dictionary
d1={'a':"apple",
    'b':"banana",
    'n':{1: "one", 2: "two", 3: "three"},
    'c':"carrot"}
d1['n'][1]="dictionary"
print(d1['n'][1])   
print(d)                       


#10: Initialize dictionary with default values
keys = ['a', 'b', 'c']
d = dict.fromkeys(keys, 0)


#11: Create a dictionary by extracting the keys from a given dictionary
d = {
    'a': 10,
    'b': 20,
    'c': 30
}
p=[]
p=d.keys()
p=dict(dict.fromkeys(p,1))
print(p)

#12: Delete a list of keys from a dictionary
d = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}
d.pop('a')
d.pop('b')
print(d)



#13: Check if a value exists in a  dictionary
d={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
s=input("enter the values")
if s in d.values():
     print("presnent")
else:
     print("not")   


#14: Rename key of a dictionary
d={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
d[10] = d.pop(1)   # Rename key 1 to 10
print(d)


#15: Get the key of a minimum value
d = {10: 'ten', 2: 'two', 5: 'five'}
print(min(d))



#16: Change value of a key in a nested dictionary
d1={'a':"apple",
    'b':"banana",
    'n':{1: "one", 2: "two", 3: "three"},
    'c':"carrot"}
d1['n'][1]="ust"
print(d1['n'][1])       


#17: Invert Dictionary
d={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
k={}
l1=[]
l2=[]
for x in d.keys():
    l1.append(x)
print(l1)
for x in d.values():
    l2.append(x)
print(l2)
for x,y in zip(l1,l2):
    k[y]=x
print(k)
    

#18: Sort Dictionary by Keys
d = { 2: 'two',10: 'ten', 5: 'five'}
d=dict(sorted(d.items()))
print(d)


#19: Sort Dictionary by Values
d = {2: 'two', 10: 'ten', 5: 'five'}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)



#20: Check if All Values are Unique
d={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'two'}
k=[]
c=0
for x in d.values():
    if x not in k:
        k.append(x)
        c=c+1
    else:
        print(x)
   
if c==len(d):
    print("values are unique")
else:
    print("not")'''









    




