"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:list of numbers
# 2. Process:the list is built by hand and then sorted and the last item is removed
# 3. Out:the whole list, one item of my choice, the list sorted, and something computed from it
# 4. What my list is about, and what I computed from it:list of numbers and I computed the last item in the list after sorting it. The last item is interesting because it is the largest number in the list.


# Your code below
number_1 = 10
number_2 = 45
number_3 = 68
number_4 = 93
number_5 = 73
number_6 = 99

print(number_1)
print(number_2)
print(number_3)
print(number_4)
print(number_5)
print(number_6)

list = [44, 58, 61, 73, 8, 9, 19, 11, 2, 1]

print(list)
print(list[3])

list.sort()
print("Sorted list:", list)

list.pop()
print("List after removing last item:", list)