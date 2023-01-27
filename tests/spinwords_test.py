import unittest

from spinwords import spinWords, reverseWord

class TestSpinwords(unittest.TestCase):
    def test_reversing_one_word(self):
        self.assertEqual("olleh", reverseWord("hello"))

    def test_one(self):
        self.assertEqual("Hey wollef sroirraw", spinWords("Hey fellow warriors"))


"""spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""