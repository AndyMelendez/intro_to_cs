# Project: CS61A Homework 4
# Name: Krishna Parashar
# Login: cs61a-wh
# TA: Julia Oh
# Section: 11


# Q1: Define a function reverse_list that takes a list as an argument and returns None, but reverses the elements in the list as a side effect. Do not use any built-in list methods (especially not reverse), but assignment statements are fine:

def reverse_list(s):
    """Reverse the contents of list s and return None.

    >>> digits = [6, 2, 9, 5, 1, 4, 1, 3]
    >>> reverse_list(digits)
    >>> digits
    [3, 1, 4, 1, 5, 9, 2, 6]
    >>> d = digits
    >>> reverse_list(d)
    >>> digits
    [6, 2, 9, 5, 1, 4, 1, 3]
    """
    counter, k = 0, len.s
    if counter <= len.s:
        s[k] = s[k - 1]
        k += 1
        counter += 1
    return None

f = digits = [6, 2, 9, 5, 1, 4, 1, 3]
reverse_list(digits)
print (f)



# Q2:  Define a function make_accumulator that returns an accumulator function, which takes one numerical argument and returns the sum of all arguments ever passed to accumulator. Use a list and not a nonlocal statement:

def make_accumulator():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"


# Q3: Define a function make_accumulator_nonlocal that returns an accumulator function, which takes one numerical argument and returns the sum of all arguments ever passed to accumulator. Use a nonlocal statement, but no list or dict:

def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and
    accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    "*** YOUR CODE HERE ***"


# Q4: Define a function make_counter that returns a counter function, which takes an immutable key and a numerical value argument and returns the sum of all arguments ever passed to counter with that same key:

def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a', 3)
    3
    >>> c('a', 5)
    8
    >>> c('b', 7)
    7
    >>> c('a', 9)
    17
    >>> c2 = make_counter()
    >>> c2(1, 2)
    2
    >>> c2(3, 4)
    4
    >>> c2(3, c('b', 6))
    17
    """
    "*** YOUR CODE HERE ***"


# Q5: Define the repeated function from Homework 2 by calling reduce with compose1 as the first argument. Add only a single expression to the starter implementation below:

def square(x):
    return x*x

def compose1(f, g):
    """Return a function of x that computes f(g(x))."""
    return lambda x: f(g(x))

from functools import reduce

def repeated(f, n):
    """Return the function that computes the nth application of f, for n>=1.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    assert type(n) == int and n > 0, "Bad n"
    return reduce(compose1, "*** YOUR CODE HERE ***" )


# Q6: Define a function shuffle that takes a list with an even number of elements (cards) and creates a new list that interleaves the elements of the first half with the elements of the second half:

def card(n):
    """Return the playing card type for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> suits = ['â™¡', 'â™¢', 'â™¤', 'â™§']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    >>> cards[26:30]
    ['7â™¤', '7â™§', '8â™¡', '8â™¢']
    >>> shuffle(cards)[:12]
    ['Aâ™¡', '7â™¤', 'Aâ™¢', '7â™§', 'Aâ™¤', '8â™¡', 'Aâ™§', '8â™¢', '2â™¡', '8â™¤', '2â™¢', '8â™§']
    >>> shuffle(shuffle(cards))[:12]
    ['Aâ™¡', '4â™¢', '7â™¤', '10â™§', 'Aâ™¢', '4â™¤', '7â™§', 'Jâ™¡', 'Aâ™¤', '4â™§', '8â™¡', 'Jâ™¢']
    >>> cards[:12]  # Should not be changed
    ['Aâ™¡', 'Aâ™¢', 'Aâ™¤', 'Aâ™§', '2â™¡', '2â™¢', '2â™¤', '2â™§', '3â™¡', '3â™¢', '3â™¤', '3â™§']
    >>> repeated(shuffle, 8)(cards) == cards
    True
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    "*** YOUR CODE HERE ***"

