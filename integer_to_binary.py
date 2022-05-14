# Problem Statement
# convert integer values to their binary equivalent.

from ds.stack import Stack

def convert_i2b(int_num):
    s = Stack()
    binary_str = ""
    
    if(int_num == 0):
        return 0
    
    while int_num > 0:
        s.push(int_num % 2)
        int_num = int_num // 2
    
    while not s.is_empty():
        binary_str += str(s.pop())

    return binary_str



print(convert_i2b(33))
print(int(convert_i2b(33))==33)
    
