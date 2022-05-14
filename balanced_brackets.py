# Problem statement
# A balanced set of brackets is one where the number and type of opening and closing brackets match and that is also properly nested within the string of brackets

from ds.stack import Stack

def is_match(x, y):
    if(x == "(" and y == ")"):
        return True
    elif(x == "{" and y == "}"):
        return True
    elif(x == "[" and y == "]"):
        return True
    else:
        return False

def is_paren_balanced(paren):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren) and is_balanced:
        curr = paren[index]
        if curr in "[({":
            s.push(curr)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, curr):
                    is_balanced = False
                    break
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else: 
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))
