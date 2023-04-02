""" Classes """


class NotADocument(Exception):
    """ This exeption ocures when we pass not a document to cursor """
class UnvalidCharacter(Exception):
    """ This exeption ocures when unvalid character is passed in document """
class EmptyDocDeleting(Exception):
    """ This exeption ocures we try to delete character from empty document """

class Document:
    """ Document class """
    def __init__ (self):
        """ Init document """
        self.characters = []
        self.cursor = Cursor(self)
        self.filename =  ''

    def insert (self, character):
        """ Insert character to document """
        if not hasattr(character, "character"):
            character = Character(character)
        self.characters.append(character)
        self.cursor.position = len(self.characters) - 1

    def delete(self):
        """ Delete character """
        self.cursor.position = min(self.cursor.position, len(self.characters) - 1)
        if len(self.characters) == 0:
            raise EmptyDocDeleting
        del self.characters[self.cursor.position]

    def save(self):
        """ Save document """
        with open("test.txt", 'w') as file:
            line = ""
            for character in self.characters:
                line += str(character)
            file.write(line)

    def forward(self):
        """ Set cursor one step forward """
        self.cursor.forward()

    @property
    def string(self):
        """ Getter property which returns string representation of document characters """
        return "".join((str(character) for character in self.characters))

    def back(self):
        """ Set cursor one step backward """
        self.cursor.back()


class Cursor:
    """ Cursor class """
    def __init__ (self, document):
        """ Init cursor """
        if not isinstance(document, Document):
            raise NotADocument
        self.document = document
        self.position= 0

    def forward(self):
        """ Set cursor one step forward """
        self.position += 1

    def back(self):
        """ Set cursor one step backward """
        self.position -= 1

    def home(self):
        """ Set cursor home """
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline break
                break

    def end(self):
        """ Set character to the end """
        while self.position< len(self.document.characters)\
        and self.document.characters[self.position].character != '\n':
            self.position += 1

class Character:
    """ Character class """
    def __init__(self, character,bold = False, italic = False, underline= False):
        """ Init character """
        if not isinstance(character, str):
            raise UnvalidCharacter
        if len(character) != 1:
            raise UnvalidCharacter
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """ Convert object inctance to string """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character

document = Document()
document.insert("h")
document.insert("e")
document.insert(Character('l', bold=True, italic=True))
document.insert(Character('l', bold=True))
document.insert("o")
document.save()
