from django.test import TestCase
"""The assertEqual() to check for an expected result; 
    assertTrue() or assertFalse() to verify a condition; 
    assertRaises() to verify that a specific exception gets raised. 
    ASSERT statement so the test runner can accumulate all test results and produce a report.
    setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. 
"""
# Create your tests here.
import unittest
from appdigilib.views import CateSerach


class Test_Articles(unittest.TestCase):

    def test(self):
        raise AssertionError()

    """def setUp(self):
        print("Preparando el contexto")
        categorys = ['Ranking', 'Flow']
        analitictask=['Sumarized', 'Labeled']
        article= ['Sandeep Reddivari, Zhangji Chen, Nan Niu','ReCVisu: A tool for clustering-based visual exploration of requirements',
                   '10.1109/RE.2012.6345828', 'Clustering is of great practical value in discovering natural groupings of large numbers of requirements artifacts.',
                   '28/09/2012', 'Clustering', 'Correletion','']
                   
        def tearDown(self):
            print("Destruyendo el contexto")
             del(self.numeros)
    """

    def Test_Search_False_of_Category_in_Article(self):
        # input
        article = ['Sandeep Reddivari, Zhangji Chen, Nan Niu',
                   'ReCVisu: A tool for clustering-based visual exploration of requirements',
                   '10.1109/RE.2012.6345828',
                   'Clustering is of great practical value in discovering natural groupings of large numbers of requirements artifacts.',
                   '28/09/2012', 'Clustering', 'Correletion', '']
        categorys = 'Ranking'

        #act
        result= CateSerach(article, categorys)

        #assert
        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()