# 61A Homework 5
# Name: Krishna Parashar and Andrea Melendez
# Login: cs61a-wh and cs61a-akz
# TA: Julia Oh
# Section: 11

class VendingMachine(object):
    """A vending machine that vends some product for some price.
        
        >>> v = VendingMachine('crab', 10)
        >>> v.vend()
        'Machine is out of stock.'
        >>> v.restock(2)
        'Current crab stock: 2'
        >>> v.vend()
        'You must deposit $10 more.'
        >>> v.deposit(7)
        'Current balance: $7'
        >>> v.vend()
        'You must deposit $3 more.'
        >>> v.deposit(5)
        'Current balance: $12'
        >>> v.vend()
        'Here is your crab and $2 change.'
        >>> v.deposit(10)
        'Current balance: $10'
        >>> v.vend()
        'Here is your crab.'
        >>> v.deposit(15)
        'Machine is out of stock. Here is your $15.'
        """

    def __init__(self, name, cost):
        self.vending_machine_works = True
        self.given_money = 0
        self.stock = 0
        self.name = name
        self.cost = cost
    
    def restock(self, put_in_stock):
        if put_in_stock > 0:
            self.stock = put_in_stock
            return "Current " + self.name + " stock: " + str(self.stock)
        else:
            self.stock = 0
    
    def vend(self):
        if self.stock == 0:
            return "Machine is out of stock."
        else:
            if self.given_money == self.cost:
                self.stock -= 1
                self.given_money = 0
                return "Here is your " + self.name + "."
            elif self.given_money < self.cost:
                needed_money = self.cost - self.given_money
                return "You must deposit $" + str(needed_money) + " more."
            else: #self.deposit > self.cost
                self.stock -= 1
                change = self.given_money - self.cost
                self.given_money = 0
                return "Here is your " + self.name + " and $" + str(change) + " change."

    def deposit(self, deposit_money):
        assert deposit_money > 0, "Deposit must be larger than zero"
        if self.stock == 0:
            return "Machine is out of stock. Here is your $" + str(deposit_money) + "."
        else:
            self.given_money += deposit_money
            return "Current balance: $" + str(self.given_money)

# Q2.

class MissManners(object):
    """A container class that only forward messages that say please.
        
        >>> v = VendingMachine('teaspoon', 10)
        >>> v.restock(2)
        'Current teaspoon stock: 2'
        >>> m = MissManners(v)
        >>> m.ask('vend')
        'You must learn to say please.'
        >>> m.ask('please vend')
        'You must deposit $10 more.'
        >>> m.ask('please deposit', 20)
        'Current balance: $20'
        >>> m.ask('now will you vend?')
        'You must learn to say please.'
        >>> m.ask('please give up a teaspoon')
        'Thanks for asking, but I know not how to give up a teaspoon'
        >>> m.ask('please vend')
        'Here is your teaspoon and $10 change.'
        """
    def __init__(self, v):
        self.v = v
    
    def ask(self, *args):
        if len(args) == 1:
            what_you_said=args[0]
            if what_you_said == "please vend":
                return self.v.vend()
            elif what_you_said[0:6]== "please":
                return "Thanks for asking, but I know not how to" + what_you_said[6:]
            else:
                return "You must learn to say please."
        elif len(args) ==2:
            what_you_said=args[0]
            money=args[1]
            return self.v.deposit(money)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
"TO PERFORM THE DOCTEST: cd Desktop, cd Fall 2012, cd Hw, python -m doctest hw5.py"



# Q3.

class Amount(object):
    """An amount of nickels and pennies.
        
        >>> a = Amount(3, 7)
        >>> a.nickels
        3
        >>> a.pennies
        7
        >>> a.value
        22
        >>> a.nickels = 5
        >>> a.value
        32
        """
    "*** YOUR CODE HERE ***"
    def __init__(self, nick, pen):
        self.nickels = nick
        self.pennies = pen
    @property
    def value(self):
        return self.nickels*5 + self.pennies

class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than
        four pennies, by converting excess pennies to nickels.
        
        >>> a = MinimalAmount(3, 7)
        >>> a.nickels
        4
        >>> a.pennies
        2
        >>> a.value
        22
        """
    def __init__(self, nick, pen):
        Amount.__init__(self, nick, pen)
        minimal_amount = 4
        if self.pennies > minimal_amount:
            self.nickels += (self.pennies)//5
            self.pennies = self.pennies%5


# Q4.

class Container(object):
    """A container for a single item.
        
        >>> c = Container(12)
        >>> c
        Container(12)
        >>> len(c)
        1
        >>> c[0]
        12
        """
    
    def __init__(self, item):
        self._item = item
    
    def __repr__(self):
        return 'Container({0})'.format(repr(self._item))
    
    def __len__(self):
        return 1
    
    def __getitem__(self, index):
        assert index == 0, 'A container holds only one item'
        return self._item

class Rlist(object):
    """A recursive list consisting of a first element and the rest.
        
        >>> s = Rlist(1, Rlist(2, Rlist(3)))
        >>> len(s)
        3
        >>> s[0]
        1
        >>> s[1]
        2
        >>> s[2]
        3
        """
    
    def __init__(self, *args):
        if len(args) == 1:
            self.first = args[0]
            self.rest = None
        elif len(args)==2:
            self.first = args[0]
            self.rest = args[1]
    def __len__(self):
        """Return the length of recursive list s."""
        length = 1
        while self.rest != None:
            self, length = self.rest, length + 1
        return length
    def __getitem__(self, index):
        assert index >= 0, 'Non-negative index'
        """Return the element at index i of recursive list s."""
        while index > 0:
            self, index = self.rest, index - 1
        return self.first
