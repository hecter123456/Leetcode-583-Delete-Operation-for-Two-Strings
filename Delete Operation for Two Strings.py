import unittest

class unitest(unittest.TestCase):
    def testEmptyWord(self):
        word1 = ""
        word2 = ""
        self.assertEqual(Solution().minDistance(word1,word2),0);

class Solution():
    def minDistance(self, word1, word2):
        if (not len(word1)) or (not len(word2)):
            return 0 

if __name__ == '__main__':
    unittest.main()
