import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.indexminpq import IndexMinPQ



class TestWaveNetModule_shapes(unittest.TestCase):

    def test_getdelmin(self):
        strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]
        pq = IndexMinPQ(len(strings))
        for idx, st in enumerate(strings):
            pq.insert(idx, st)
        self.assertEqual("best", pq.getMin())  
        self.assertEqual(10, pq.size())  
        
        min_list =[]
        for _ in range(len(strings)):
            min = pq.delMin()
            min_list.append(min)
        self.assertTrue(pq.isEmpty())

        ground_truth = ["best", "it", "it", "of", "the", "the", "times", "was", "was", "worst"]
        #ground_truth = ["best", "it", "it", "of", "the", "the", "times",  "was"]

        self.assertEqual(min_list, ground_truth)
        


    def test_getdelmin(self): 
            strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]
            pq = IndexMinPQ(len(strings))
            for idx, st in enumerate(strings):
                pq.insert(idx, st)
            pq.changeindex(3, "just")

            self.assertEqual("it", pq.getMin())  
            self.assertEqual(10, pq.size())  

            pq.changeindex(7, "alpha")
            self.assertEqual("alpha", pq.getMin()) 
            _ = pq.delMin()
            




    




if __name__ == '__main__':
    unittest.main()