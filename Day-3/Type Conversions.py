Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> 
>>> b=75.2
>>> int(b)
75
>>> complex(b)
(75.2+0j)
>>> str(b)
'75.2'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True

c=75+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(75+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True

s="Indu"
s="2456"
s="456.789"
int(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '456.789'

s="Indu"
a='1234'
b='13.45'
int(a)
1234
float(b)
13.45
list(s)
['I', 'n', 'd', 'u']
list(a)
['1', '2', '3', '4']
list(b)
['1', '3', '.', '4', '5']
tuple(s)
('I', 'n', 'd', 'u')
tuple(a)
('1', '2', '3', '4')
tuple(b)
('1', '3', '.', '4', '5')
set(a)
{'1', '2', '3', '4'}
set(b)
{'4', '.', '1', '5', '3'}
set(s)
{'d', 'n', 'I', 'u'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(a)
True
bool(b)
True
bool(s)
True

l=[1,2,3,4]
l
[1, 2, 3, 4]
int(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    complex(l)
TypeError: complex() argument must be a string or a number, not list
tuple(l)
(1, 2, 3, 4)
set(l)
{1, 2, 3, 4}
bool(l)
True

t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
str(t)
'(1, 2, 3, 4, 5)'
list(t)
[1, 2, 3, 4, 5]
tuple(t)
(1, 2, 3, 4, 5)
bool(t)
True

s={1,2,3}
s
{1, 2, 3}
str(s)
'{1, 2, 3}'
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
bool(s)
True

b=True
int(b)
1
float(b)
1.0
complex(b)
(1+0j)
str(b)
'True'

d={'name':'indu','age':'21'}
d
{'name': 'indu', 'age': '21'}
str(d)
"{'name': 'indu', 'age': '21'}"
list(d)
['name', 'age']
tuple(d)
('name', 'age')
set(d)
{'name', 'age'}
bool(d)
True
