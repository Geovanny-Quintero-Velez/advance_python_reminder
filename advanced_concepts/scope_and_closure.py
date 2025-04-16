"""
Scope define how far a variable can be reached.
also how encapsulated is it into the method.
Scope defines two types of variable: Local and global

Closure define 
"""

def local_function():
    x = 10 # local variable
    print(f'Variable\'s value is {x}')

local_function()
print(x) # generates error

# ---
x = 100
def show_global():
    print(f'Global Variable value is {x}')

print(x)


# --- Closures --- 
def outer_function():
    def inner_function():
        print("inner")
    inner_function()
    print("outer")
outer_function()