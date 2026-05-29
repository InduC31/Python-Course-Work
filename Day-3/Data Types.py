Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
type(a)
<class 'int'>
t = 999.99
type(t)
<class 'float'>
c = 12+8j
type(c)
<class 'complex'>
s='Python'
type(s)
<class 'str'>
s="Full Stack"
type(s)
<class 'str'>
s='''Python Full Stack'''
type(s)
<class 'str'>
s='Python'
s='Java'
s
'Java'
s='Python'
id(s)
2812853157008
s='Java'
id(s)
2812859547744
l=[1,2,3,4]
id(l)
2812896198528
l.append(50)
l.append(60)
l
[1, 2, 3, 4, 50, 60]
id(l)
2812896198528
l=[1,2,3]
l
[1, 2, 3]
>>> l=['post1.png','reel1.mp4']
>>> l
['post1.png', 'reel1.mp4']
>>> l=[]
>>> l=l=[1,2,3,4]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,34,5,6,67)
>>> t
(1, 2, 34, 5, 6, 67)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,6}
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={45678,546,3456,13423}
>>> a
10
>>> s
{3456, 546, 45678, 13423}
>>> s={1,1,1,1,1,1,4}
>>> s
{1, 4}
>>> d = {'name':'abc','age':'100','course':'PFS')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> d
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d = {'name':'abc','age':'100','course':'PFS'}
>>> d
{'name': 'abc', 'age': '100', 'course': 'PFS'}
>>> type(d)
<class 'dict'>
>>> status = True
>>> ststus = False
>>> status = False
>>> type(status)
<class 'bool'>
>>> a = None
>>> type(a)
<class 'NoneType'>
