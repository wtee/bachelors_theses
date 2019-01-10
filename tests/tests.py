import unittest

from process_theses import deslash_author_statement, deslash_title, truecase, needs_truecase, final_styling_for_title, final_styling_for_author, make_245_c, make_245_a

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

    def test_needs_truecase(self):
        # Test authors
        test_string1 = "by HERBERT CHARLES FLINT and WILLIAM FRANCIS LAGRANGE"
        test_string2 = "By A. A. Baustian, H. D. Susong, and E. Young"
        # Test titles
        test_string3 = "An Investigation of Industrial Housing"
        test_string4 = "A study of the decomposition of green manures."

        self.assertTrue(needs_truecase(test_string1, "author"))
        self.assertFalse(needs_truecase(test_string2, "author"))
        self.assertTrue(needs_truecase(test_string3, "title"))
        self.assertFalse(needs_truecase(test_string4, "title"))

    def test_final_styling_for_title(self):
        test_string = "A study of the decomposition of green manures."
        desired = "A study of the decomposition of green manures /"

        result = final_styling_for_title(test_string)

        self.assertEqual(result, desired)
    
    def test_final_styling_for_author(self):
        test_string = "By A. A. Baustian, H. D. Susong, and E. Young"
        desired = "by A. A. Baustian, H. D. Susong, and E. Young."

        result = final_styling_for_author(test_string)

        self.assertEqual(result, desired)

    def test_make_245_c(self):
        test_string1 = "BY HERBERT CHARLES FLINT \ WILLIAM FRANCIS LAGRANGE"
        test_string2 = "by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."

        desired1 = "by Herbert Charles Flint and William Francis Lagrange."
        desired2 = "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."

        result1 = make_245_c(test_string1)
        result2 = make_245_c(test_string2)

        self.assertEqual(result1, desired1)
        self.assertEqual(result2, desired2)

    def test_make_245_a(self):
        test_string1 = "A Genetic Analysis \ of \ a Rabbit Stock as regards the \ Color Factor"
        test_string2 = "COST ACCOUNT STUDY OF AN IOWA FARM \ 1918 - 1919."

        desired1 = "A genetic analysis of a rabbit stock as regards the color factor /"
        desired2 = "Cost account study of an Iowa farm 1918 - 1919 /"

        result1 = make_245_a(test_string1)
        result2 = make_245_a(test_string2)

        self.assertEqual(result1, desired1)
        self.assertEqual(result2, desired2)