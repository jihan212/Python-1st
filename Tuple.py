Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ('Python','Java','C','C#','C++','2121','1999')
>>> type(a)
<class 'tuple'>
>>> a[0]
'Python'
>>> type(a[0])
<class 'str'>
>>> type(a[6])
<class 'str'>
>>> a[6]
'1999'
>>> type(1999)
<class 'int'>
>>> a =('Python','Java','C','C#','C++',2121,1999)
>>> type(a[0])
<class 'str'>
>>> type(a[6])
<class 'int'>
>>> a[a:5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[a:5]
TypeError: slice indices must be integers or None or have an __index__ method
>>> a[0:5]
('Python', 'Java', 'C', 'C#', 'C++')
>>> a[6:]
(1999,)
>>> a[5:]
(2121, 1999)
>>> a +(3.1416)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a +(3.1416)
TypeError: can only concatenate tuple (not "float") to tuple
>>> a + (3.1416,)
('Python', 'Java', 'C', 'C#', 'C++', 2121, 1999, 3.1416)
>>> type(a[7])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    type(a[7])
IndexError: tuple index out of range
>>> type(a[6])
<class 'int'>
>>> len (a)
7
>>> 
