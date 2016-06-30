
#1- TEXT EDITOR
'''
text editor recommeded for osx in pythoncrashcourse is sublime text
pg 9 configuring text editor to version of python
terminal command: type -a python3 to view path /usr/local/bin/python3)
'''

#2- APPEND PATH
'''
it seems like I appended the path,
but not able to add the folder to PATH BROWSER or CLASS BROWSER

>> sys.path.append(/Users/einatkorman/Documents/python_tutorials)
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> sys.path.append('/Users/einatkorman/Documents/python_tutorials')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sys.path.append('/Users/einatkorman/Documents/python_tutorials')
NameError: name 'sys' is not defined
>>> import sys
>>> sys.path.append('/Users/einatkorman/Documents/python_tutorials')
>>> import os
>>> os.getcwd()
'/Users/einatkorman/Documents/python_tutorials'
'''

#3- IMPORT SUBPROCESS, IMPORT OS SYS 
'''
subprocess runs other functions / can call any file?
is there a place to see the code within these modules so I can see what it is actually doing?
same with the afplay other pyaudio or any other module that you run as a function.
I don't mind using a module in the code, that can be really efficient,
but I'd like to be able to read through what it is doing, more than just a definition.
'''

#4- SORTED REVERSE
'''
sorted() temporarily sorts a list in numerical/alphabetical order.
book says that it will accept a reverse=True argument,
cannot get it to work without error.


