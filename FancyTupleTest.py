import unittest
from fancy_tuple_class import FancyTuple

class FancyTupleTest(unittest.TestCase):

    def test_min_attribute(self):
        fancy_tuple = FancyTuple("dog")
        self.assertEqual(fancy_tuple.first, "dog")
        print("Minimum attribute ran fine.")

    def test_max_attribute(self):
        fancy_tuple = FancyTuple("dog","mouse","cat","horse","python")
        self.assertEqual(fancy_tuple.fifth, "python")
        print("Class max attribute works")
        
    def test_len_class(self):
        fancy_tuple = FancyTuple("dog","mouse","cat","horse","python")
        self.assertEqual(len(fancy_tuple),5)
        print("Class __len__ method works")


if __name__ == '__main__':
    unittest.main()