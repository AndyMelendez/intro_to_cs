# 61A Homework 7
# Name: Krishna Parashar and Andrea Melendez
# Login: cs61a-wh and cs61a-akz
# TA: Julia Oh
# Section: 11

# Q1.

class Square(object):
    def __init__(self, side):
        self.side = side

class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def type_tag(s):
    return type_tag.tags[type(s)]

type_tag.tags = {Square: 's', Rect: 'r'}

def apply(operator_name, shape):
    """Apply operator to shape.
        
        >>> apply('area', Square(10))
        100
        >>> apply('perimeter', Square(5))
        20
        >>> apply('area', Rect(5, 10))
        50
        >>> apply('perimeter', Rect(2, 4))
        12
        """
    tag = (type_tag(shape))
    key = (operator_name, tag)
    return apply.implementations[key](shape)

apply.implementations = {('area', 's'): lambda square: square.side*square.side, 
                         ('perimeter', 's'): lambda square: square.side*4, 
                         ('area', 'r'): lambda rectangle: rectangle.width*rectangle.height, 
                         ('perimeter', 'r'): lambda rectangle: rectangle.width*2 + rectangle.height*2}

# Q2.

def g(n):
    """Return the value of G(n), computed recursively.
        
        >>> g(1)
        1
        >>> g(2)
        2
        >>> g(3)
        3
        >>> g(4)
        10
        >>> g(5)
        22
        """
    if (n <= 3):
        return n
    else:
        return g(n - 1) +  (2 * g(n - 2)) + (3 * g(n - 3))

def g_iter(n):
    """Return the value of G(n), computed iteratively.
        >>> g_iter(1)
        1
        >>> g_iter(2)
        2
        >>> g_iter(3)
        3
        >>> g_iter(4)
        10
        >>> g_iter(5)
        22
        """
    total, k = [], 0
    while (k <= n):
        if (k <= 3):
            total.append(k)
            k += 1
        elif (k > 3):
            total.append(total[k - 1] + (2 * total[k - 2]) + (3 * total[k - 3]))
            k += 1
    return total[n]

# Q3.

def part(n):
    """Return the number of partitions of positive integer n.
        
        >>> part(5)
        7
        >>> part(10)
        42
        >>> part(15)
        176
        >>> part(20)
        627
    """

    def memo(f):
        cache = {}
        def memoized(*args):
            if args not in cache:
                cache[args] = f(*args)
            return cache[args]
        return memoized
	
    @memo
    def partition(n, base_value):
        if (n < base_value):
            return 0
        if (n == base_value):
            return 1
        return partition(n - base_value, base_value) + partition(n, base_value + 1)
    return partition(n, 1)

# Q4.

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.
        
        >>> make_anonymous_factorial()(5)
        120
        """
    return lambda n: 1 if n == 1 else mul(n, make_anonymous_factorial()(sub(n, 1)))

x = make_anonymous_factorial()(201)
print (x)

# Q5.

def has_cycle(s):
    """Return whether Rlist s contains a cycle.
        
        >>> s = Rlist(1, Rlist(2, Rlist(3)))
        >>> s.rest.rest.rest = s
        >>> has_cycle(s)
        True
        >>> t = Rlist(1, Rlist(2, Rlist(3)))
        >>> has_cycle(t)
        False
        """
    "*** YOUR CODE HERE ***"

def has_cycle_constant(s):
    """Return whether Rlist s contains a cycle.
        
        >>> s = Rlist(1, Rlist(2, Rlist(3)))
        >>> s.rest.rest.rest = s
        >>> has_cycle_constant(s)
        True
        >>> t = Rlist(1, Rlist(2, Rlist(3)))
        >>> has_cycle_constant(t)
        False
        """
    "*** YOUR CODE HERE ***"

class Rlist(object):
    """A recursive list consisting of a first element and the rest."""
    class EmptyList(object):
        def __len__(self):
            return 0
    
    empty = EmptyList()
    
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)
    
    def __len__(self):
        return 1 + len(self.rest)
    
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i-1]


