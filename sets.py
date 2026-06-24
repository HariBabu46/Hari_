'''#1: Perform Basic Set Operations
s={4,6,1,2,3,4,5,6,7,8}
print(s)


#2: Union of Sets
s1={1,2,3,4}
s2={5,6,7,8}
k=s1.union(s2)
print(k)


#3: Intersection of Sets
s1={1,2,3,4,7,8}
s2={5,6,7,8,9,10}
p=s1.intersection(s2)
print(p)

#4: Difference of Sets
s1={1,2,3,4,7,8}
s2={5,6,7,8,9,10}
p=s1.difference(s2)
print(p)

#5: Symmetric Difference
s1={1,2,3,4,7,8}
s2={5,6,7,8,9,10}
p=s1.symmetric_difference(s2)
print(p)                


#6: Add a list of Elements to a Set
s1={1,2,3,4}
l=list(s1)
print(l)
d=[6,7,8,9]
for  i in d:
    l.append(i)
print(l)  

#7: Set Difference Update
s1={1,2,3,4,7,8}
s2={5,6,7,8,9,10}
p=s1.difference_update(s2)
print(p)  


#8: Remove Items From Set Simultaneously
numbers = {1, 2, 3, 4, 5, 6}
numbers.difference_update({2, 4, 6})
print(numbers)

#9: Check Subset
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

#10: Check Superset
A = {1, 2}
B = {1, 2, 3, 4}
print(B.issuperset(A))

#11: Set Intersection Check
set1 = {10, 20, 30}
set2 = {30, 40, 50}
if set1.intersection(set2):
    print("Sets have common elements")
else:
    print("No common elements")


#12: Set Symmetric Difference Update
set1 = {10, 20, 30}
set2 = {30, 40, 50}
p=s1.symmetric_difference_update(s2)
print(p)


#13: Set Intersection Update
set1 = {10, 20, 30}
set2 = {30, 40, 50}
p=s1.intersection_update(s2)
print(p)         '''

#14: Find Common Elements in Two Lists
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common = list(set(list1) & set(list2))
print(common)

#15: Frozen Set
numbers = frozenset([10, 20, 30, 40])
print(numbers)


#16: Count Unique Words
s = "apple banana apple orange banana grape"
words = s.split()
u = set(words)
print(u)
print("Unique word count:", len(u))