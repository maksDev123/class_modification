
""" Test classes """
import unittest
from classes import Document, Character, Cursor,\
NotADocument, UnvalidCharacter, EmptyDocDeleting

class TestClasses(unittest.TestCase):
    """ Test Document, Cursor and Character classes """
    def test_inctance_creation(self):
        """ Test inctance creation """
        document = Document()
        self.assertIsInstance(document, Document)
        cursor = Cursor(document)
        self.assertIsInstance(cursor, Cursor)
        character = Character("a")
        self.assertIsInstance(character, Character)

        with self.assertRaises(NotADocument):
            _ = Cursor(1)
        with self.assertRaises(UnvalidCharacter):
            _ = Character(1, 2, 3)
        with self.assertRaises(UnvalidCharacter):
            _ = Character("asd")
        with self.assertRaises(UnvalidCharacter):
            _ = Character([])

    def test_character_insertion(self):
        """ Test character insertion """
        document = Document()
        document.insert("h")
        document.insert("e")
        document.insert(Character('l', bold=True))
        document.insert(Character('l', bold=True))
        document.insert("o")
        document.insert("\n")
        document.insert(Character('w', italic=True))
        document.insert(Character('o', italic=True))
        document.insert(Character('r', underline=True))
        document.insert("l")
        document.insert("d")

        self.assertEqual(document.string, """he*l*lo\n/w/o_rld""")

    def test_unvalid_character_insertion(self):
        """ Test invalid character exeption """
        document = Document()

        with self.assertRaises(UnvalidCharacter):
            document.insert(Character("test", bold=True))
        with self.assertRaises(UnvalidCharacter):
            document.insert("test")
        with self.assertRaises(UnvalidCharacter):
            document.insert([1, 2, 3])
        with self.assertRaises(UnvalidCharacter):
            document.insert(Character([1, 2, 3]))
        with self.assertRaises(UnvalidCharacter):
            document.insert([])

    def test_cursor(self):
        """ Test cursor """
        document = Document()
        document.insert("h")
        document.insert("e")
        document.insert(Character('l', bold=True))
        document.insert(Character('l', bold=True))
        document.insert("o")
        document.insert("\n")
        document.insert(Character('w', italic=True))
        document.insert(Character('o', italic=True))
        document.insert(Character('r', underline=True))
        document.insert("l")
        document.insert("d")

        self.assertEqual(document.cursor.position, 10)
        document.cursor.home()
        self.assertEqual(document.cursor.position, 6)
        document.characters[0].underline = True
        self.assertEqual(document.string, """_he*l*lo\n/w/o_rld""")
        document.cursor.home()
        self.assertEqual(document.cursor.position, 6)
        document.back()
        document.cursor.home()
        self.assertEqual(document.cursor.position, 0)
        document.forward()
        self.assertEqual(document.cursor.position, 1)
        document.cursor.end()
        self.assertEqual(document.cursor.position, 5)
        document.delete()
        self.assertEqual(document.string, """_he*l*lo/w/o_rld""")
        document.save()

    def test_deleting(self):
        """ Test deleting """
        document = Document()
        document.insert("h")
        document.insert("e")
        document.insert(Character('l', bold=True))
        document.insert(Character('l', bold=True))
        document.insert("o")

        self.assertEqual(document.string, """he*l*lo""")
        document.delete()
        self.assertEqual(document.string, """he*l*l""")
        document.delete()
        self.assertEqual(document.string, """he*l""")
        document.delete()
        self.assertEqual(document.string, """he""")
        document.delete()
        self.assertEqual(document.string, """h""")
        document.delete()
        self.assertEqual(document.string, """""")
        with self.assertRaises(EmptyDocDeleting):
            document.delete()

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
