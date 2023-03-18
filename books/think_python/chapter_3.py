# Exercise 1: Creates a function called right_justify which receives a string called S as parameter and shows a
# number of spaces before in a way that the last letter os the word ends in column 70 of the screen
def right_justify(s):
    print(len(s))
    print(s)


right_justify(" " * 65 + "monty")


# Exercise 2: Testing a function example
# Test A)
def do_twice_a(f):
    f()
    f()


def print_spam():
    print("spam")


do_twice_a(print_spam)


# Test B)
def do_twice_b(f, g):
    print(type(f))
    print(g)


do_twice_b("Spam",  20)
do_twice_b("Spam", 20)


# Test C)
def do_twice_c(f, g):
    print(type(f))
    print(g)


def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice_c(print_twice("spam"), print_twice("spam"))


# Test D)
def do_four(f, g):
    print(type(f))
    print(g)


do_four("spam", "spam")
do_four("spam", "spam")
do_four("spam", "spam")
do_four("spam", "spam")


# Exercise 3: Testing what was learned from chapter 1 to 3
# Test A)
def grid():
    print("+" + "-"*4 + "+" + "-"*4 + "+")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("+" + "-"*4 + "+" + "-"*4 + "+")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("|" + " "*4 + "|" + " "*4 + "|")
    print("+" + "-"*4 + "+" + "-"*4 + "+")


grid()


# Test B)
def grid_2():
    print(("+" + "-"*4)*4 + "+")
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("+" + "-"*4)*4 + "+")
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("+" + "-"*4)*4 + "+")
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("+" + "-"*4)*4 + "+")
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|" + " "*4 + "|"))
    print(("+" + "-"*4)*4 + "+")


grid_2()
