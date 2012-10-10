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

    initial = 0
    final = (len(s) - 1)
    temp = s[initial]
    while initial <= len(s) and final >= 0:
	    temp = s[initial]
	    s[initial] = s[final]
	    s[final] = temp
	    initial += 1
	    final -= 1 
	    if (initial >= final or final < initial):
	        break
    return None


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
    total = []
    def accumalator(argument):
        total.append(argument)
        return sum(total)
    return accumalator


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
    total = 0
    def accumulator(amount):
        nonlocal total          
        total = total + amount                 
        return total
    return accumulator

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
    table = {}
    def counter(key, value):
        nonlocal table
        if key in list(table):
            table[key] = table[key] + value
        else:
            table[key] = value
        return table[key]
    return counter


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
    return reduce(compose1, [f]*n)


# Q6: Define a function shuffle that takes a list with an even number of elements (cards) and creates a new list that interleaves the elements of the first half with the elements of the second half:

def card(n):
    """Return the playing card type for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards.

    >>> suits = ['♡', '♢', '♤', '♧']
    >>> cards = [card(n) + suit for n in range(1,14) for suit in suits]
    >>> cards[:12]
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> cards[26:30]
    ['7♤', '7♧', '8♡', '8♢']
    >>> shuffle(cards)[:12]
    ['A♡', '7♤', 'A♢', '7♧', 'A♤', '8♡', 'A♧', '8♢', '2♡', '8♤', '2♢', '8♧']
    >>> shuffle(shuffle(cards))[:12]
    ['A♡', '4♢', '7♤', '10♧', 'A♢', '4♤', '7♧', 'J♡', 'A♤', '4♧', '8♡', 'J♢']
    >>> cards[:12]  # Should not be changed
    ['A♡', 'A♢', 'A♤', 'A♧', '2♡', '2♢', '2♤', '2♧', '3♡', '3♢', '3♤', '3♧']
    >>> repeated(shuffle, 8)(cards) == cards
    True
    """
    assert len(cards) % 2 == 0, 'len(cards) must be even'
    shuffled = []
    for i in range(0, len(cards)):
	    shuffled.append(cards[i])
	
	first_half = card[0 : len(cards)/2]
	second_half = card[0 : len(cards)/2 : len(cards)]

suits = ['♡', '♢', '♤', '♧']
cards = [card(n) + suit for n in range(1,14) for suit in suits]
x = cards[:12]
print (x)
y = cards[26:30]
print(y)
z = shuffle(cards)[:12]
print(z)