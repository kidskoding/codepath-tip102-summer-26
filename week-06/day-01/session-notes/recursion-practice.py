def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

def reverse_string(s):
    if len(s) <= 1:
        return s
    rest = s[:-1]
    print(rest)
    return s[-1] + reverse_string(rest)
    
print(reverse_string("apple"))

def list_length(node):
    if node is None:
        return 0
    return 1 + list_length(node.next)
    
def test(n):
    if n == 0:
        return 1
    return n * test(n-1)
    
print(test(5))