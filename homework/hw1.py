#Q1. Recall that we can assign new names to existing functions. Fill in the blanks in the following function definition for adding a to the absolute value of b, without calling abs.

print('Question 1:')

from operator import mul, add, sub
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

x = a_plus_abs_b(2, 3)
y = a_plus_abs_b(2, -3)

print (x)
print (y)
print('All tests passed!\n')


#Q2. Write a function that takes three positive numbers and returns the sum of the squares of the two largest numbers. Use only a single expression for the body of the function:
	
print('Question 2:')

def two_of_three(a, b, c):
    """
    Return x*x + y*y, where x and y are the two largest of a, b, c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    max1 = max(a, b)
    max2 = max(b, c)
	
    ans = add
    return ans(max1*max1, max2*max2)

a = two_of_three(1, 2, 3)
b = two_of_three(5, 3, 1)
c = two_of_three(10, 2, 8)
d = two_of_three(5, 5, 5)

print (a)
print (b)
print (c)
print (d)
print('All tests passed!\n')



#Q3. Let's try to write a function that does the same thing as an if statement:
	
print('Question 3:')

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True
   
def t():
    return print("True")

def f():
    return 1
   
with_if_statement()
with_if_function()

print('All tests passed!\n')



#Q4. Douglas Hofstadter’s Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

#Pick a positive integer n as the start.
#If n is even, divide it by 2.
#If n is odd, multipy it by 3 and add 1.
#Continue this process until n is 1.

print('Question 4:')

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    while n != 1 :
        if n%2==0 :
            n = n/2
            print(n)
        else :
            n = (n*3)+1
            print(n)

hailstone(10)

print('All tests passed!\n')