from ExpMatch import isMatch 
import unittest 

class TestPatterns(unittest.TestCase):
    
    def test(self):
        self.assertEqual(True,isMatch("aa","a*"))
        self.assertEqual(True,isMatch("aaa","a*"))
        self.assertEqual(True,isMatch("aaab","a*b"))
        self.assertEqual(True,isMatch("abc","abc*"))
        self.assertEqual(True,isMatch("abcccd","a.c*d"))
        self.assertEqual(True,isMatch("",""))
        self.assertEqual(True,isMatch("abcd","a*bc."))
        self.assertEqual(False,isMatch("abcd","ab*d"))
        self.assertEqual(True,isMatch("abcee","abce*."))

if __name__ == '__main__':
    unittest.main()