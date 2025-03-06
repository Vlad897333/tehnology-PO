import unittest
import Test_2 # type: ignore
class py_test(unittest.TestCase):
    def test_string(self):
       self.assertEqual(Test_2.back_string('Hello'),' olleH')

    def test_string(self):
       self.assertEqual(Test_2.back_string('ars'),'sra')

    def test_string(self):
       self.assertEqual(Test_2.back_string('rs'),'sr')

    def test_string(self):
       self.assertEqual(Test_2.back_string('World'),'dlroW')

    def test_string(self):
       self.assertEqual(Test_2.back_string('Ket'),'teK')

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('Masha'),('Masha'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('set'),('tes'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('meell'),('mell'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('med'),('med'))

    def test_polindroms(self):
        self.assertEqual(Test_2.polindrome('well'),('llew'))

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Домик'),1)

    def test_vowels(self):
        self.assertEqual(Test_2.vowels('Мусор'), 3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Кот'),3)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Имя'),2)

    def test_vowels(self):
       self.assertEqual(Test_2.vowels('Государь'),2)

    
    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("hell"), "hll")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("nows"), "ns")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("qweqweqwe"), "qwe")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("sasasa"), "sa")

    def test_remove_duplicates(self):
        self.assertEqual(Test_2.remove_duplicates("rtrtrt"), "tr")


if __name__ == 'main':
    unittest.main()
