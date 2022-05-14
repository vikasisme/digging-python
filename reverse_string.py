from ds.stack import Stack

def reverse_string(input_str):
    s = Stack()
    reverse_str = ""
    for i in range(len(input_str)):
        s.push(input_str[i])
    while not s.is_empty(): 
        reverse_str += s.pop()
    
    return reverse_str

print("Reversing strings....")
print(reverse_string('sakiv'))