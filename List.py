Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ['Python','C','C#','C++','Java']
>>> a
['Python', 'C', 'C#', 'C++', 'Java']
>>> type(a)
<class 'list'>
>>> a[0]
'Python'
>>> a[4]
'Java'
>>> a[:2]
['Python', 'C']
>>> a[2:]
['C#', 'C++', 'Java']
>>> type
<class 'type'>
>>> type(a[0])
<class 'str'>
>>> a[4]='JavaScript'
>>> a
['Python', 'C', 'C#', 'C++', 'JavaScript']
>>> a.append('Java')
>>> a
['Python', 'C', 'C#', 'C++', 'JavaScript', 'Java']
>>> a.remove('JavaSCript')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.remove('JavaSCript')
ValueError: list.remove(x): x not in list
>>> a.remove('JavaScript')
>>> a
['Python', 'C', 'C#', 'C++', 'Java']
>>> a.append('JavaScript')
>>> a.remove('Java')
>>> a
['Python', 'C', 'C#', 'C++', 'JavaScript']
>>> a.insert (4,'Java')
>>> a
['Python', 'C', 'C#', 'C++', 'Java', 'JavaScript']
>>> b = ['HTML','CSS','JQuarey','SQL']
>>> a = a+b
>>> a
['Python', 'C', 'C#', 'C++', 'Java', 'JavaScript', 'HTML', 'CSS', 'JQuarey', 'SQL']
>>> a.remove('C')
>>> a.remove('C#')
>>> a.remove('C++')
>>> a
['Python', 'Java', 'JavaScript', 'HTML', 'CSS', 'JQuarey', 'SQL']
>>> a.extend(['C','C#','C++'])
>>> a
['Python', 'Java', 'JavaScript', 'HTML', 'CSS', 'JQuarey', 'SQL', 'C', 'C#', 'C++']
>>> len.a
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    len.a
AttributeError: 'builtin_function_or_method' object has no attribute 'a'
>>> len.(a)
SyntaxError: invalid syntax
>>> len(a)
10
>>> a.count('Python')
1
>>> a.reverse()
>>> a
['C++', 'C#', 'C', 'SQL', 'JQuarey', 'CSS', 'HTML', 'JavaScript', 'Java', 'Python']
>>> a.sort()
>>> a
['C', 'C#', 'C++', 'CSS', 'HTML', 'JQuarey', 'Java', 'JavaScript', 'Python', 'SQL']
>>> 
