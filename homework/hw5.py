"""61A Homework 5
Name: Krishna Parashar and Andrea Melendez
Login: cs61a-wh and cs61a-akz
TA: Julia Oh
Section: 11
"""

# Q1.

def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.


    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    value, total = None, 0
    def counted_add(num1, num2):
        nonlocal value
        value = f(num1, num2)
        return value
    
    def add_count():
        nonlocal value, total
        if  value is None:
            total = total
        else:
            total += 1
            value = None
        return total
    return counted_add, add_count


# Q2.

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    attempts = []
    def withdraw(withdrawal, attempted_password):
        nonlocal balance, attempts
        if password == attempted_password and len(attempts) < 3:
            if balance >= withdrawal:
                balance -= withdrawal
                return balance
            else:
                print('Insufficient funds')
        else:
            attempts += [attempted_password]
            if len(attempts) <= 3:
                print('Incorrect password')
            else:
                print('Your account is locked. Attempts:', attempts[:3])
    return withdraw


# Q3.

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    storing=withdraw(0, old_password)
    if type(storing) != str:
        def joint(new_amount_to_withdraw, second_password_checking):
            if second_password_checking == new_password: #first way to access the balance
                return withdraw(new_amount_to_withdraw, old_password)
            elif second_password_checking == old_password: #second way to access the balance
                return withdraw(new_amount_to_withdraw, old_password)
            else:
                return withdraw(new_amount_to_withdraw, second_password_checking)
        return joint
    else:
        return storing
