# Index

```python
index_list = [1, 2, 3, 4, 5, 6]
```

### positive index

```python
print(index_list[0]) # 1
print(index_list[1]) # 2
print(index_list[4]) # 5
```

### negative index

```python
print(index_list[-1]) # 6
print(index_list[-5]) # 2
print(index_list[-6]) # 1
```

### enumerate

```python
# syntax - enumerate(iter, start=0)
# return - (num, item)
enum = list(enumerate(grocery_list, 1))
print(enum) # [(1, 'onion'), (2, 'tomato'), (3, 'carrot'), (4, 'potato')]

for item_num, grocery in enumerate(grocery_list, 1):
print(item_num, '. ', grocery, sep='') # 1. onion # 2. tomato # 3. carrot # 4. potato
```

# slicing

```python
x_list = [10, 20, 30, 60, 70, 80, 90]

y_list = x_list[2:5]
print(y_list) # [30, 60, 70]

z_list = x_list[3:]
print(z_list) # [60, 70, 80, 90]

k_list = x_list[2:5:2]
print(k_list) # [30, 70]

q_list = x_list[:3]
print(q_list) # [10, 20, 30]
```

### insert into slice

```python
my_list = [10, 20, 30, 40, 50, 60]
my_list[1:4] = [707, 777]
print(my_list) # [10, 707, 777, 50, 60]
```

### insert into start of array

```python
my_list = [1, 2, 3, 4]
my_list[0:0] = [-50, -40]
print(my_list) # [-50, -40, 1, 2, 3, 4]
```

# List Operations

```python
list1 + list2 # Produces a new list containing the contents of both list1 and list2 by performing concatenation.

list1 * n, orn * list1 # Produces a list containing the contents of list1, repeated n times.
# example
x_list = [0] * 3
print(x_list) # [0, 0, 0].

list[n] # Indexing.

list[begin:end:hop] # Slicing

# pass by reference
list1 = list2 # list1 becomes an alias for list2.

# example
a_list = [1, 2, 3, 4]
b_list = a_list
b_list.append(100)
a_list.append(200)
b_list.append(300)
print(a_list) # list now equals [1, 2, 3, 4, 100, 200, 300]


list1 = list2[:] # perform a member-by-member copy of list2
#example
grocery_list = ['onion', 'tomato', 'carrot', 'potato']
new_list = grocery_list[:]
print(new_list)

list1 == list2 # Produces True if list1 and list2 have equal contents, after performing a member-by-member comparison.

list1 != list2 # Produces False if list1 and list2 have equal contents; True otherwise.

elem in list # Produces True if elem is an element of list.
elem not in list # Produces True if elem is not an element of list.
#example
a = [1, 2, 3]
None in a # False
[] in a # False

b = [1, 2, 3, [], None]
None in b # True
[] in b # True

```

# List Methods

```python
list.append(value) # Append a value.
#example
a_list = [1, 2, 3]
a_list.append(4) # [1, 2, 3, 4]

list.clear() # Remove all contents.

list.extend(iterable) # Append a series of values.
#example
a_list = [1, 2, 3]
a_list.extend([4]) # [1, 2, 3, 4]
a_list.extend([4, 5, 6])  # [1, 2, 3, 4, 5, 6]

list.insert(index, value) # At index, insert value.
#example
a_list = [10, 20, 40]
a_list.insert(2, 30 )
print(a_list) # [10, 20, 30, 40]

list.remove(value) # Remove first instance of value.
#example
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list) # list now equals [2, 3]

the_scores = [1.0, 3.5, 1.0, 6.0, 1.0, 7.0]
the_scores.remove(1)
print(the_scores) # list now equals [3.5, 1.0, 6.0, 1.0, 7.0]

list.sort([key=None] [, reverse=False])
#example
num_list = [3, 2, 17, 2.5]
num_list.sort()
print(num_list) # Sorts into [2, 2.5, 3, 17]

a_list = [ 'john', 'paul', 'George', 'brian', 'Ringo' ]
b_list = a_list[:]
a_list.sort()
print(a_list) # ['George', 'Ringo', 'brian', 'john', 'paul']
b_list.sort(key=ignore_case)
print(b_list) # ['brian', 'George', 'john', 'paul', 'Ringo']

list.reverse()      # Reverse existing order.
#example
a_list.reverse()
print(a_list) # [300, 200, 100, 4, 3, 2, 1]
```

# List Funtions

```python
len(collection)       # Return length of the collection
max(collection)       # Return the elem with maximum value.
min(collection)       # Return the elem with minimum value.
reversed(collection)  # Produce iter in reversed order.
sorted(collection)    # Produce list in sorted order.
sum(collection)       # Adds up all the elements, which must be numeric.
```
