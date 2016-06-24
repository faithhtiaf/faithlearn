
import unittest

class TestStringMethods(unittest.TestCase):
    def test_supper(self):

        self.assertEqual('foo'.upper(), 'FOO')

    def testIsSuppet(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def testSplit(self):
        s='hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
suit=unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
unittest.TextTestRunner(verbosity=2).run(suit)