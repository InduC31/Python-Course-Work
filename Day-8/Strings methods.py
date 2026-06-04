Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> s='    hello     world     '
>>> s
'    hello     world     '
>>> s.strip()
'hello     world'
>>> s.lstrip()
'hello     world     '
>>> s.rstrip()
'    hello     world'
>>> 
>>> s='strings.py'
>>> s
'strings.py'
>>> s.startswith('str')
True
>>> s.startswith('gfh')
False
>>> s.endswith('py')
True
>>> s.endswith('js')
False
>>> 'sdfyui'.isalpha()
True
>>> 'DSFGHJkftrryghjutyghj'.isalpha()
True
>>> 'sowmya@11234354'.isalpha()
False
>>> '2345678'.ialnum()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    '2345678'.ialnum()
AttributeError: 'str' object has no attribute 'ialnum'. Did you mean: 'isalnum'?
>>> '2345678'.isalnum()
True
>>> 'sfdxgchvjbkn'.isalnum()
True
>>> 'indu23456'.isalnum()
True
>>> 'ewrtyuii'.isalnum()
True
>>> 'dfghj345678@#$%^&*'.islower()
True
>>> 'ASDFGH@#$%%^&&'.isupper()
True
>>> ' '.isspace()
True
'hello                 '.isspace()
False
'Py Prg Lan'.istitle()
True
'Py prg lan'.istitle()
False
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
