import unittest
from Prj1PassChecker import passWdLength, passUpLow, passNumb, passSpecials

class TestPasswordFunctions(unittest.TestCase):
    def test_passWdLength(self):
        self.assertTrue(passWdLength("StrongPass12!"))
        self.assertFalse(passWdLength("short"))
        self.assertFalse(passWdLength("ThisIsAVeryLongPassword123!"))

    def test_passUpLow(self):
        self.assertTrue(passUpLow("HelloWorld123!"))
        self.assertFalse(passUpLow("helloworld123!"))
        self.assertFalse(passUpLow("HELLOWORLD123!"))

    def test_passNumb(self):
        self.assertTrue(passNumb("Password1!"))
        self.assertFalse(passNumb("Password!"))
    
    def test_passSpecials(self):
        self.assertTrue(passSpecials("Hgn@!sLni2141"))
        self.assertFalse(passSpecials("832nJBN3knkfsj"))

if __name__ == '__main__':
    unittest.main()
