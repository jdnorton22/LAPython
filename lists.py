my_list=[1,2,3,4,5]
other_list=['a', 2, True, 4.5]


print(my_list[2])

# not code
>>> my_list=[1,2,3,4,5]
>>> my_list[4]
5
>>> my_list[:2]
[1, 2]
>>> my_list[::2]
[1, 3, 5]
>>> my_list[0]='a'
>>> my_list[::1]
['a', 2, 3, 4, 5]
>>> my_list += [8,9,10]
>>> my_list
['a', 2, 3, 4, 5, 8, 9, 10]
>>> my_list[1:3] = ['b','c']
>>> my_list
['a', 'b', 'c', 4, 5, 8, 9, 10]
>>> del my_list[3]
>>> my_list
['a', 'b', 'c', 5, 8, 9, 10]
>>>
>>> >>> my_list=[1,2,3,4,5]
  File "<stdin>", line 1
    >>> my_list=[1,2,3,4,5]
    ^
SyntaxError: invalid syntax
>>> >>> my_list[4]
  File "<stdin>", line 1
    >>> my_list[4]
    ^
SyntaxError: invalid syntax
>>> 5
5
>>> >>> my_list[:2]
  File "<stdin>", line 1
    >>> my_list[:2]
    ^
SyntaxError: invalid syntax
>>> [1, 2]
[1, 2]
>>> >>> my_list[::2]
  File "<stdin>", line 1
    >>> my_list[::2]
    ^
SyntaxError: invalid syntax
>>> [1, 3, 5]
[1, 3, 5]
>>> >>> my_list[0]='a'
  File "<stdin>", line 1
    >>> my_list[0]='a'
    ^
SyntaxError: invalid syntax
>>> >>> my_list[::1]
  File "<stdin>", line 1
    >>> my_list[::1]
    ^
SyntaxError: invalid syntax
>>> ['a', 2, 3, 4, 5]
['a', 2, 3, 4, 5]
>>> >>> my_list += [8,9,10]
  File "<stdin>", line 1
    >>> my_list += [8,9,10]
    ^
SyntaxError: invalid syntax
>>> >>> my_list
  File "<stdin>", line 1
    >>> my_list
    ^
SyntaxError: invalid syntax
>>> ['a', 2, 3, 4, 5, 8, 9, 10]
['a', 2, 3, 4, 5, 8, 9, 10]
>>> >>> my_list[1:3] = ['b','c']
  File "<stdin>", line 1
    >>> my_list[1:3] = ['b','c']
    ^
SyntaxError: invalid syntax
>>> >>> my_list
  File "<stdin>", line 1
    >>> my_list
    ^
SyntaxError: invalid syntax
>>> ['a', 'b', 'c', 4, 5, 8, 9, 10]
['a', 'b', 'c', 4, 5, 8, 9, 10]
>>> >>> del my_list[3]
  File "<stdin>", line 1
    >>> del my_list[3]
    ^
SyntaxError: invalid syntax
>>> >>> my_list
  File "<stdin>", line 1
    >>> my_list
    ^
SyntaxError: invalid syntax
>>> my_list = [1,2,3]           
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]
>>> my_list.insert(0,'a')
>>> my_list
['a', 1, 2, 3, 4]
>>> my_list.index(3)
3
>>> my_list = [1,2,3]
>>> my_list.index(2)
1
>>> 4 in my_list
False
>>> 4 is not in my_list
  File "<stdin>", line 1
    4 is not in my_list
             ^
SyntaxError: invalid syntax
>>> 4 not in my_list
True
>>> 2 in my_list
True
>>> my_list=[1,3,4,8,2]
>>> sorted(my_list)
[1, 2, 3, 4, 8]
>>> new_list=sorted(my_list)
>>> new_list
[1, 2, 3, 4, 8]
>>> reversed(my_list)
<list_reverseiterator object at 0x00000243FF793C70>
>>> reversed(my_list)
<list_reverseiterator object at 0x00000243FF793C40>
>>> list(reversed(my_list)
... 
KeyboardInterrupt
>>> list(reversed(my_list))
[2, 8, 4, 3, 1]
>>> list(reversed(sorted(my_list)))
[8, 4, 3, 2, 1]
>>> new_list
[1, 2, 3, 4, 8]