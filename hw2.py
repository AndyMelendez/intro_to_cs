"""61A Homework 2
Name: Krishna Parashar
Login:
TA:
Section: 11
"""
# Q1.

print ('Q1:')

def square(x):
    """Return x squared."""
    return x * x

def itself(x):
    """Return x itself."""
    return x

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    total, k = 1, 1
    while k <= n:
	    total = total*term(k)
	    k = k + 1
    return total
	
check1 = product(4, square)
print ('4!^2 =', check1,)


def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    return product(n, itself)

check2 = factorial(4)	
print ('4! =', check2, '\n')



# Q2.

print ('Q2:')

from operator import mul, add

def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    k = 1
    total = start
    while k <= n:
        total = combiner(term(k), total)
        k = k + 1
    return total


def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    return accumulate(mul, 1, n, term)

check3 = summation_using_accumulate(4, square)
check4 = product_using_accumulate(4, square)
print (check3)
print (check4, '\n')


# Q3.

print ('Q3:')

def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    def term(x):
        return f(f(x))
    return term

test5 = double(square)(2)
print (test5, '\n')

# Q4.

print ('Q4:')

def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    counter = 1
    g = f
    while counter < n:
	    g = compose1(g, f)
	    counter = counter + 1
    return g


def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

test6 = repeated(square, 2)(5)
test7 = repeated(square, 4)(5)
print (test6)
print (test7, '\n')

# Q5. 
# Note: Extra for Experts

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"

def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n."""
    "*** YOUR CODE HERE ***"

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> three = successor(two)
    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"


