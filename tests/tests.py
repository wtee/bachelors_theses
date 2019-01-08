import unittest

from process_theses import deslash_author_statement, deslash_title, truecase

class UtilsTests(unittest.TestCase):
    def test_deslash_author_statement(self):
        test_string = "by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."
        desired = "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."
        result = deslash_author_statement(test_string)
        self.assertEqual(result, desired)
    
    def test_deslash_title(self):
        test_string = "A Genetic Analysis \ of \ a Rabbit Stock as regards the \ Color Factor"
        desired = "A Genetic Analysis of a Rabbit Stock as regards the Color Factor"
        result = deslash_title(test_string)
        self.assertEqual(result, desired)

    def test_trucase_title(self):
        test_string1 = "HISTORY OF THE TYPE CHANGE OF THE POLAND-CHINA BREED."
        test_string2 = "A STUDY OF THE DECOMPOSITION OF GREEN MANURES."
        test_string3 = "SEASONAL PROFILE VARIATION OF AN EARTH ROAD."
        test_string4 = "An Investigation of Industrial Housing"

        desired1 = "History of the type change of the Poland-China Breed."
        desired2 = "A study of the decomposition of green manures."
        desired3 = "Seasonal profile variation of an earth road."
        desired4 = "An investigation of industrial housing"

        result1 = truecase(desired1)
        result2 = truecase(desired2)
        result3 = truecase(desired3)
        result4 = truecase(desired4)

        self.assertEqual(result1, desired1)
        self.assertEqual(result2, desired2)
        self.assertEqual(result3, desired3)
        self.assertEqual(result4, desired4)


    def test_trucase_author_statement(self):
        test_string1 = "by HERBERT CHARLES FLINT and WILLIAM FRANCIS LAGRANGE"
        test_string2 = "BY OTMAR W. ZACK"
        test_string3 = "by A. A. BAUSTIAN, H. D. SUSONG, and E. YOUNG"

        desired1 = "By Herbert Charles Flint and William Francis Lagrange"
        desired2 = "By Otmar W. Zack"
        desired3 = "By A. A. Baustian, H. D. Susong, and E. Young"

        result1 = truecase(desired1)
        result2 = truecase(desired2)
        result3 = truecase(desired3)

        self.assertEqual(result1, desired1)
        self.assertEqual(result2, desired2)
        self.assertEqual(result3, desired3)