import unittest
import numpy as np

class unitest(unittest.TestCase):
    def testEmptyWord(self):
        word1 = ""
        word2 = ""
        self.assertEqual(Solution().minDistance(word1,word2),0);
    def testExampleWord(self):
        word1 = "sea"
        word2 = "eat"
        self.assertEqual(Solution().minDistance(word1,word2),2);

class Solution():
    def minDistance(self, word1, word2):
        w = len(word1)
        h = len(word2)
        if not h or not w:
            return 0
        exW = w+1
        exH = h+1
        Matrix = [[0 for x in range(exW)] for y in range(exH)] 
        for x in range(exW):
            for y in range(exH):
                if not x or not y:
                    Matrix[x][y] = 0
                elif word1[x-1] == word2[y-1]:
                    Matrix[x][y] = Matrix[x-1][y-1]+1
                else:
                    Matrix[x][y] = max(Matrix[x-1][y],Matrix[x][y-1])
        print(np.matrix(Matrix))
        return w+h-(Matrix[w][h]*2)
if __name__ == '__main__':
    unittest.main()
