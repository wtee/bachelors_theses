import unittest

from process_theses import deslash

class UtilsTests(unittest.TestCase):
    def test_deslash(self):
        test_string = "by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."
        desired = "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."
        result = deslash(test_string)
        self.assertEqual(result, desired)