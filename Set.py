Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {'Python','Java','C','C#','C++'}
>>> type(a)
<class 'set'>
>>> b = set('HTML','CSS','JQuarey')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b = set('HTML','CSS','JQuarey')
TypeError: set expected at most 1 arguments, got 3
>>> b = set ('HTML')
>>> a
{'C#', 'Java', 'Python', 'C', 'C++'}
>>> b
{'M', 'H', 'T', 'L'}
>>> c = set ()
>>> type (c)
<class 'set'>
>>> c
set()
>>> d = {}
>>> type(d)
<class 'dict'>
>>> a
{'C#', 'Java', 'Python', 'C', 'C++'}
>>> a[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[0]
TypeError: 'set' object is not subscriptable
>>> a.add('HTML')
>>> a
{'C#', 'Java', 'Python', 'C', 'HTML', 'C++'}
>>> a.update('CSS'.'JQuarey')
SyntaxError: invalid syntax
>>> a.update('CSS','Jquarey')
>>> a
{'C#', 'e', 'Java', 'q', 'Python', 'C', 'y', 'r', 'HTML', 'C++', 'J', 'S', 'a', 'u'}
>>> a.remove('e')
>>> a
{'C#', 'Java', 'q', 'Python', 'C', 'y', 'r', 'HTML', 'C++', 'J', 'S', 'a', 'u'}
>>> a.remove('q')
>>> a.remove('C')
>>> a.remove('y')
>>> a.remove('r')
>>> a.remove('J')
>>> a.remove('S')
>>> a.remove('a')
>>> a.remove('u')
>>> a
{'C#', 'Java', 'Python', 'HTML', 'C++'}
>>> a.update({'CSS','JQuarey'})
>>> a
{'C#', 'Java', 'Python', 'JQuarey', 'CSS', 'HTML', 'C++'}
>>> a.discard('1999')
>>> a
{'C#', 'Java', 'Python', 'JQuarey', 'CSS', 'HTML', 'C++'}
>>> a.pop()
'C#'
>>> a
{'Java', 'Python', 'JQuarey', 'CSS', 'HTML', 'C++'}
>>> a.clear()
>>> a
set()
>>> ype(a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    ype(a)
NameError: name 'ype' is not defined
>>> type(a)
<class 'set'>
>>> a = {1,2,3,4,5}
>>> b = {3,4,5,6,7}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7}
>>> a.intersection(b)
{3, 4, 5}
>>> a.difference(b)
{1, 2}
>>> a
{1, 2, 3, 4, 5}
>>> 
