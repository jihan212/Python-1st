Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = {}
>>> type(a)
<class 'dict'>
>>> a = {'Name':'Daniel Redcliff','Charecter':'Harry Potter'}
>>> a
{'Name': 'Daniel Redcliff', 'Charecter': 'Harry Potter'}
>>> b = dict('Name':'Kishor', 'Surname':'Pasha')
SyntaxError: invalid syntax
>>> a
{'Name': 'Daniel Redcliff', 'Charecter': 'Harry Potter'}
>>> a['name']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a['name']
KeyError: 'name'
>>> a['Name']
'Daniel Redcliff'
>>> a['Name']='Emma Watson'
>>> a
{'Name': 'Emma Watson', 'Charecter': 'Harry Potter'}
>>> a['Charecter']
'Harry Potter'
>>> a['Charecter']= 'Hermionie'
>>> a
{'Name': 'Emma Watson', 'Charecter': 'Hermionie'}
>>> a['School']= 'Hogwarts'
>>> a
{'Name': 'Emma Watson', 'Charecter': 'Hermionie', 'School': 'Hogwarts'}
>>> b = {'Best Friend':'Harry & Ron'}
>>> a.update(b)
>>> a
{'Name': 'Emma Watson', 'Charecter': 'Hermionie', 'School': 'Hogwarts', 'Best Friend': 'Harry & Ron'}
>>> del a['Best Friend']
>>> a
{'Name': 'Emma Watson', 'Charecter': 'Hermionie', 'School': 'Hogwarts'}
>>> a.clear()
>>> a
{}
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = {'Name':'Kishor','Surname':'Pasha','Home':'Rocky Beach','Best Friends':'Robin & Musa'}
>>> a
{'Name': 'Kishor', 'Surname': 'Pasha', 'Home': 'Rocky Beach', 'Best Friends': 'Robin & Musa'}
>>> a.copy()
{'Name': 'Kishor', 'Surname': 'Pasha', 'Home': 'Rocky Beach', 'Best Friends': 'Robin & Musa'}
>>> a.get('Name')
'Kishor'
>>> a.get('Best Friends')
'Robin & Musa'
>>> a.get('Uncle')
>>> a.get('Uncle','Rashed Pasha')
'Rashed Pasha'
>>> a.get('Uncle')
>>> 'Name' in a
True
>>> 'Mother' in a
False
>>> a.items()
dict_items([('Name', 'Kishor'), ('Surname', 'Pasha'), ('Home', 'Rocky Beach'), ('Best Friends', 'Robin & Musa')])
>>> a.keys()
dict_keys(['Name', 'Surname', 'Home', 'Best Friends'])
>>> a.values()
dict_values(['Kishor', 'Pasha', 'Rocky Beach', 'Robin & Musa'])
>>> 
