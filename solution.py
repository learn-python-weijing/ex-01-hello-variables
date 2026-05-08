# Exercise 01 — Hello, World & Variables
# Fill in each function. Do NOT change the function names or parameters.

#======================Task 1====================================
def greet(name):
    """Return a greeting string: "Hello, <name>!" """
    pass


def add(a, b):
    """Return the sum of a and b."""
    pass


def is_even(n):
    """Return True if n is even, False otherwise."""
    pass


def circle_area(radius):
    """Return the area of a circle with the given radius.
    Use 3.14159 for pi. Round the result to 2 decimal places.
    """
    pass

#======================Task 2====================================

def double(x):
    #return double of the value x
    pass

def square(x):
    #return square of the value x
    pass

def negate(x):
    #flips the sign of x: e.g. negate(-1) --> 1, negate(1) --> -1
    pass

def increment(x):
    #adds 1 to x
    pass

def decrement(x):
    #subtracts 1 from x
    pass

#======================Task 3====================================
#Use the compose function declared below to complete the functions
#Each function to only have 1 line, which is the return line

#DO NOT CHANGE
def compose(f1, f2):
    #both f1 and f2 to be unary functions
    #will be in the format f2(f1(x))
    return lambda x: f2(f1(x))

def double_then_square(x):
    pass

def square_then_double(x):
    pass

def negate_then_square(x):
    pass

def increment_then_double(x):
    pass

def double_then_negate(x):
    pass

def double_square_negate(x):
    pass

def inc_inc_double(x):
    pass
