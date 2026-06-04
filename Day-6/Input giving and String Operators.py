Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name = input()
Indu
>>> name
'Indu'
>>> name = input("Enter the name:")
Enter the name: Indu
>>> name
' Indu'
>>> age = input("Enter your age:")
Enter your age:21
>>> age
'21'
>>> age = int(input("Enter your age:"))
Enter your age: 21
>>> age
21
>>> type(age)
<class 'int'>
>>> gpa = floag(input("ENter the cpa:"))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    gpa = floag(input("ENter the cpa:"))
NameError: name 'floag' is not defined. Did you mean: 'float'?
>>> gpa = float(input("ENter the cpa:"))
ENter the cpa:7.9
>>> gpa
7.9
>>> type(gpa)
<class 'float'>
>>> 'indu kusuma usha'
'indu kusuma usha'
>>> 'indu kusuma usha'.split('')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    'indu kusuma usha'.split('')
ValueError: empty separator
>>> 'indu kusuma usha'.split(' ')
['indu', 'kusuma', 'usha']
>>> 'java-python-c-c++-javascript'.split('-')
['java', 'python', 'c', 'c++', 'javascript']
>>> names = input("Enter the names:").split()
Enter the names:laptop mouse charger keyboard
>>> names
['laptop', 'mouse', 'charger', 'keyboard']
>>> products = input("Enter the products:").split()
Enter the products:mobile charger powerbank
products
['mobile', 'charger', 'powerbank']
names = input("Enter the names:").split()
Enter the names:Indu Kusuma Usha
names
['Indu', 'Kusuma', 'Usha']
topics = tuple(input("Enter the topics:").split())
Enter the topics:token statement variable comments
topics
('token', 'statement', 'variable', 'comments')
op = set(input("Enter the oper:").split())
Enter the oper:in not or not in is is not and
op
{'or', 'and', 'is', 'in', 'not'}
marks = input("Enter the marks:").split()
Enter the marks: 34 29 56 78
marks
['34', '29', '56', '78']
int(['34', '29', '56', '78'])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(['34', '29', '56', '78'])
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
map(int,input("Enter the marks:").split())
Enter the marks:3 4 5 6 0
<map object at 0x0000021E4E65B080>
map
<class 'map'>
list(map(int,input("Enter the marks:").split()))
Enter the marks:1 2 34 56 789
[1, 2, 34, 56, 789]
prices = tuple(map(int,input("Enter the prices:").split()))
Enter the prices:4356 100 243 78 98
prices
(4356, 100, 243, 78, 98)
rating = set(map(int,input("Enter the rating:").split()))
Enter the rating: 4 5 9 8
rating
{8, 9, 4, 5}
{8, 9, 4, 5}
{8, 9, 4, 5}
per = list(map(float,input("Enter the per's : ").split()))
Enter the per's : 56.3 28.5 78.9 78.7
per
[56.3, 28.5, 78.9, 78.7]
prices = tuple(map(float,input("Enter the prices:").split()))
Enter the prices:567 345 890 2345
prices
(567.0, 345.0, 890.0, 2345.0)
prices = set(map(float,input("Enter the prices: ").split()))
Enter the prices: 3456 45678 987 567
prices
{3456.0, 987.0, 45678.0, 567.0}

a,b=10,20
a
10
b
20
a,b=(10,20)
a
10
b
20
a,b=[10,20]
a
10
b
20

username,password = input("Enter the username & password: ").split()
Enter the username & password: codegnan c@123
username
'codegnan'
password
'c@123'
a,b,c,d = list(map(int,input("Enter the 4 sides: ").split()))
Enter the 4 sides: 4 8 5 6
a
4
b
8
c
5
d
6
prices,discount = list(map(float,input().split()))
34567 70.0
prices
34567.0
discount
70.0

a=eval(input())
4567.54678
a
4567.54678
a=eval(input())
"python"
a
'python'
a=eval(input())
[1,2,3,4,5]
a
[1, 2, 3, 4, 5]
a=eval(input())
34567.9
a
34567.9
a=eval(input())
(1,2,3,4)
a
(1, 2, 3, 4)
a=eval(input())
{1,2,3,4,5}
a
{1, 2, 3, 4, 5}
a=eval(input())
{3:9,4:6,7:45}
a
{3: 9, 4: 6, 7: 45}
a=eval(input())
True
a
True
type(a)
<class 'bool'>
s='python programming lang'
s
'python programming lang'
type(s)
<class 'str'>
s=''
s
''
a='codegnan'
b='pfs'
a+b
'codegnanpfs'
a
'codegnan'
a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
'*'*20
'********************'
'Indu'*9
'InduInduInduInduInduInduInduInduIndu'
'Indu Kusuma Usha '*5
'Indu Kusuma Usha Indu Kusuma Usha Indu Kusuma Usha Indu Kusuma Usha Indu Kusuma Usha '
