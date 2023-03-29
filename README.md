# Class testing

Given repository has two files:
* classes.py - module with Document, Cursor, Character class
* test_classes.py - module with class TestClasses
### Document

Has following methods and properties:

* "__init__" - inits document
* "insert" - insert character to document
* "delete" - delete character
* "save" - saves document with name "test.txt"
* "forward" - sets cursor one step forward
* "back" - sets cursor one step backward
* "string" - returns document as string

### Cursor

Has following methods and properties:

* "__init__" - inits cursor
* "forward" - sets cursor one step forward
* "back" - sets cursor one step backward
* "home" - sets cursor home (start of the line)
* "end" - sets cursor at the end (end of current line)

### Character

Has following methods and properties:

* "__init__" - inits character
* "__str__" - represents character as string

### Exeptions
NotADocument - This exeption ocures when we pass not a document to cursor
UnvalidCharacter - This exeption ocures when unvalid character is passed in document
EmptyDocDeleting - This exeption ocures we try to delete character from empty document

### Example of usage
```
document.insert("h")
document.insert("e")
document.insert(Character('l', bold=True, italic=True))
document.insert(Character('l', bold=True))
document.insert("o")
print(document.string)
```
This will result in as "he*l*lo"

To run tests type in console:
```
python test_classes.py
```


