# sort

```python
num_list = [3, 2, 17, 2.5]
num_list.sort()
print(num_list) # Sorts into [2, 2.5, 3, 17]
```

# remove

```python
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list) # list now equals [2, 3]

the_scores = [1.0, 3.5, 1.0, 6.0, 1.0, 7.0]
the_scores.remove(1)
print(the_scores) # list now equals [3.5, 1.0, 6.0, 1.0, 7.0]
```

# pass by reference

```python
a_list = [1, 2, 3, 4]
b_list = a_list
b_list.append(100)
a_list.append(200)
b_list.append(300)
print(a_list) # list now equals [1, 2, 3, 4, 100, 200, 300]
```

# reverse

```python
a_list.reverse()
print(a_list) # list now equals [300, 200, 100, 4, 3, 2, 1]
```

# copy list

```python
grocery_list = ['onion', 'tomato', 'carrot', 'potato']
new_list = grocery_list[:]
print(new_list)
```

## Index

```python
index_list = [1, 2, 3, 4, 5, 6]
```

# positive index

```python
print(index_list[0]) # 1
print(index_list[1]) # 2
print(index_list[4]) # 5
```

# negative index

```python
print(index_list[-1]) # 6
print(index_list[-5]) # 2
print(index_list[-6]) # 1
```

# enumerate

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

# insert into slice

```python
my_list = [10, 20, 30, 40, 50, 60]
my_list[1:4] = [707, 777]
print(my_list) # [10, 707, 777, 50, 60]
```

# insert into start of array

```python
my_list = [1, 2, 3, 4]
my_list[0:0] = [-50, -40]
print(my_list) # [-50, -40, 1, 2, 3, 4]
```

# list methods

```python
list.append(value) # Append a value
list.clear() # Remove all contents
list.extend(iterable) # Append a series of values
list.insert(index, value) # At index, insert value
list.remove(value) # Remove first instance of
```
