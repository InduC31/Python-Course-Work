Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='python programming'
>>> sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
>>> min(s)
' '
>>> max(s)
'y'
>>> ord('a')
97
>>> ord('A')
65
>>> ord('0')
48
>>> ord(' ')
32
>>> chr(98)
'b'
>>> chr(120)
'x'
>>> chr(30)
'\x1e'
>>> chr(35)
'#'
>>> chr(37)
'%'
>>> chr(32)
' '
>>> chr(65)
'A'
>>> 
>>> s='python Programming'
>>> s.upper()
'PYTHON PROGRAMMING'
>>> s.lower()
'python programming'
>>> s.capitalize()
'Python programming'
>>> s.title()
'Python Programming'
>>> s.swapcase()
'PYTHON pROGRAMMING'
>>> 
>>> s
'python Programming'
>>> s.center(38,'*')
'**********python Programming**********'
s.center(28,'-')
'-----python Programming-----'
s.ljust(28,'-')
'python Programming----------'
s.rjust(28,'-')
'----------python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'

s
'python Programming'
s.find('o')
4
s.find('g')
10
s.rfind('z')
-1
s.index('o')
4
s.rindex('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s
'python Programming'
s.count('y')
1
s.count('m')
2
s.count('g')
2

s
'python Programming'
s.replace('python','java')
'java Programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 Pr5grammi6g'

s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g='''dfghjk
fghjkl;
qwerty
asdfghjkl'''
g
'dfghjk\nfghjkl;\nqwerty\nasdfghjkl'
s.splitlines()
['java,python,javascript,c,c++']
g.splitlines()
['dfghjk', 'fghjkl;', 'qwerty', 'asdfghjkl']
l=['java', 'python', 'javascript', 'c', 'c++']
''.join(1)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
''.join(l)
'javapythonjavascriptcc++'
'-'.join(l)
'java-python-javascript-c-c++'
'@'.join(l)
'java@python@javascript@c@c++'
' '.join(l)
'java python javascript c c++'
','.join(l)
'java,python,javascript,c,c++'

s
'java,python,javascript,c,c++'
s.partition(',')
('java', ',', 'python,javascript,c,c++')
s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
