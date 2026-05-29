Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=20
a+b
40
a-b
0
a*b
400
a/b
1.0
9/2
4.5
a//b
1
9//2
4
a**2
400
6**3
216
a%b
0
17%4
1
17%3
2

a
20
b
20

a=20
b=10
a
20
b
10
a<b
False
a>b
True
a<=b
False
10<=b
True
a>=b
True
a==b
False
a!=b
True

y=5
y
5
y=y+5
y
10
y=y+10
y
20
y +=10
y
30
y+=5
y
35
y+=10
\
  y
SyntaxError: unexpected indent
y
45
y-=20
y
25
y*=4
y
100
y//=10
y
10
y%=2
y
0
y/=2
y
0.0
y//=3
y
0.0
y+=10
y
10.0
y/=2
y
5.0

a=20
b=10
a
20
b
10
a%10==0
True
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
a%20==0 or b%20==0 or a<b
True
a%22==0 or b%20==0 or a<b
False
not a>b
False

#str,list,tuple,set,dict
a='python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'z' in a
False
'r' in a
True
'j' not in a
True
'r' not in a
False
l=['java','python','mysql','c++','c','html']
'mysql' in l
True
'c' not in l
False
t=('laptop','mobile','mouse','keyboard')
'charger' in t
False
'mouse' in t
True
t={1,2,4,56,7,78,235,23}
t
{1, 2, 4, 7, 235, 78, 23, 56}
4 in t
True
24 in t
False
50 not in t
True
d={'egg':8,'oil':120,'sugar':40,'salt':30}
'oil' in d
True
120 in d
False
'sugar' in d
True
'chilli' in d
False
40 in d
False

l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
>>> n==m
True
>>> l is m
False
>>> n is m
True
>>> id(l)
2217072507840
>>> id(m)
2217071340224
>>> id(n)
2217071340224
>>> l is not m
True
>>> n is not l
True
>>> 
>>> 8&14
8
>>> 8&7
0
>>> 8|7
15
>>> 10^11
1
>>> ~12
-13
>>> ~15
-16
>>> ~19
-20
>>> ~70
-71
>>> 8>>2
2
>>> 15>>1
7
>>> 15>>2
3
>>> 15>>3
1
>>> 16<<1
32
>>> 4<<2
16
