Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'tryu',[])
t
(1, 1.1, 'tryu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(90,80,70)
t+h
(10, 20, 30, 40, 50, 90, 80, 70)
t*5
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
t
(10, 20, 30, 40, 50)
t[1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
t[1]
20
t[2]
30
t[-1]
50
t[-3]
30
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t
(10, 20, 30, 40, 50)
t[3:]
(40, 50)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::2]
(10, 30, 50)
t[::-1]
(50, 40, 30, 20, 10)
t[-1:-4:-1]
(50, 40, 30)
t
(10, 20, 30, 40, 50)
10 in t
True
50 in t
True
70 in t
False
40 not in t
False
80 not in t
True
t
(10, 20, 30, 40, 50)
len(t)
5
>>> sorted(t)
[10, 20, 30, 40, 50]
>>> min(t)
10
>>> max(t)
50
>>> sum(t)
150
>>> t.count(10)
1
>>> t.index(10)
0
>>> 
>>> 
>>> t=1,2,3,4,5,6,7
>>> t
(1, 2, 3, 4, 5, 6, 7)
>>> a=(1,2,4)
>>> a
(1, 2, 4)
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
4
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[4]
7
>>> t[3]
[4, 5, 6]
>>> t[2]=4
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
