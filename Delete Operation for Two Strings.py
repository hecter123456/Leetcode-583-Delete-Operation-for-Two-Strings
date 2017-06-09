import unittest
import numpy as np

class unitest(unittest.TestCase):
    def testTwoEmptyWord(self):
        word1 = ""
        word2 = ""
        self.assertEqual(Solution().minDistance(word1,word2),0);
    def testExampleWord(self):
        word1 = "sea"
        word2 = "eat"
        self.assertEqual(Solution().minDistance(word1,word2),2);
    def testDifferentLenWord(self):
        word1 = "a"
        word2 = "ab"
        self.assertEqual(Solution().minDistance(word1,word2),1);
    def testOneEmptyWord(self):
        word1 = ""
        word2 = "a"
        self.assertEqual(Solution().minDistance(word1,word2),1);
class Solution():
    def minDistance(self, word1, word2):
        w = len(word1)
        h = len(word2)
        Matrix = [[0] * (h+1) for i in range(w+1)] 
        for x in range(w):
            for y in range(h):
                Matrix[x+1][y+1] = max(Matrix[x][y+1],Matrix[x+1][y],Matrix[x][y] + (word1[x] == word2[y]))
        print(np.matrix(Matrix))
        return w+h-(Matrix[w][h]*2)
if __name__ == '__main__':
    unittest.main()
