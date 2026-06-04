Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=(1,2,4)
s={1,2,3,4}
a
(1, 2, 4)
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,1,1,1,1,1}
s
{1}
s={987,654,345,56,345,1,2,34,6,56}
s
{1, 2, 34, 6, 654, 56, 345, 987}
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add("indu")
s
{56.567, 1, 'indu'}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add({False})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add({False})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s
{56.567, 1, 'indu'}
1 in s
True
indu in s
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    indu in s
NameError: name 'indu' is not defined. Did you mean: 'input'?
'indu' in s
True
1 is not in s
SyntaxError: invalid syntax
1 is not in s
SyntaxError: invalid syntax
s
{56.567, 1, 'indu'}


a={1,2,3,5,6,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6}
a & b
{8, 6}
a - b
{1, 2, 3, 5, 10}
a ^ b
{1, 2, 3, 5, 7, 9, 10}

a
{1, 2, 3, 5, 6, 8, 10}
#{1}{2}{3}{5}{1,3}{1,2}{8,10}
a <= {1}
False
a >= {1}
True
a <= {1,2,3,4,5,6,8,10,11,12}
True
a >= {6,8,10}
True
a
{1, 2, 3, 5, 6, 8, 10}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 5, 6, 8, 10}
a.add(17)
a
{1, 2, 3, 17, 5, 6, 8, 10}
a.add(14)
a
{1, 2, 3, 5, 6, 8, 10, 14, 17}
a.update({11,12,13})
a
{1, 2, 3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
a.pop()
1
a.pop()
2
a
{3, 5, 6, 8, 10, 11, 12, 13, 14, 17}
a.remove(6)
a
{3, 5, 8, 10, 11, 12, 13, 14, 17}
a.remove(10)
a
{3, 5, 8, 11, 12, 13, 14, 17}
a.remove(6)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.remove(6)
KeyError: 6
a.discard(3)
a
{5, 8, 11, 12, 13, 14, 17}
a.discard(6)
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> a.discard(3)
>>> a
{5, 8, 11, 12, 13, 14, 17}
>>> a.clear()
>>> a
set()
>>> a={1,23,4,57,235}
>>> b=1,2,34,4}
SyntaxError: unmatched '}'
>>> b={1,2,34,4}
>>> a.intersection(b)
{1, 4}
>>> a
{1, 4, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 4}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c
{1, 2, 4, 34}
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d=c.copy()
>>> d
{1, 2, 34, 4, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> max(c)
34
>>> min(c)
1
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
