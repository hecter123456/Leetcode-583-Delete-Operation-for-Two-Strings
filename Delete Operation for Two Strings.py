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
        exW = w+1
        exH = h+1
        Matrix = [[0 for x in range(exW)] for y in range(exH)] 
        for x in range(exH):
            for y in range(exW):
                if not x or not y:
                    Matrix[x][y] = 0
                elif word2[x-1] == word1[y-1]:
                    Matrix[x][y] = Matrix[x-1][y-1]+1
                else:
                    Matrix[x][y] = max(Matrix[x-1][y],Matrix[x][y-1])
        print(np.matrix(Matrix))
        return w+h-(Matrix[h][w]*2)
if __name__ == '__main__':
    unittest.main()
