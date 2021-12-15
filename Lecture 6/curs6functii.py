# urmeaza sa definim o functie
def product(n):
    p = 1
    for i in range(2, n+1):
        p = p * i
    return p  

p1 = product(10)
print (f"Product up to and including {10} is {p1}")


#valorile se iau in ordine

def suma(a, b, c):
    s = a+b+c
    return s


s1 = suma(1, 2, 3)
print(f"s1 = {s1}")

s1 = suma(b=1, c=2, a=3)


def function_with_variable_args(*args, **kwargs):
    print(f"args = {args}")
    print(f"kawrds = {kwargs}")
    print(f"args[0] = {args[0]}")
    print(f"kawrds[0] = {kwargs['a']}")


function_with_variable_args(1,2,3,4, a=1, b=2, c=30)

#functie cu reapelare

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))