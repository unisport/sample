import unittest
import ProductLoader

class ProductLoaderTests(unittest.TestCase):
       def testGetRangeOfListBaseOnPageNumberFirstPageMoreThan10Elements(self):
            list = [1,2,3,4,5,6,7,8,9,10,11]
            firstPage = ProductLoader.getRangeOfListBaseOnPageNumber(list, 1)
            self.assertEqual(10, len(firstPage)) 
            self.assertEqual(1, firstPage[0]) 
            self.assertEqual(10, firstPage[9]) 

       def testGetRangeOfListBaseOnPageNumberFirstPageList10Elements(self):
            list = [1,2,3,4,5,6,7,8,9,10]
            firstPage = ProductLoader.getRangeOfListBaseOnPageNumber(list, 1)
            self.assertEqual(10, len(firstPage)) 
            self.assertEqual(1, firstPage[0]) 
            self.assertEqual(10, firstPage[9]) 

       def testGetRangeOfListBaseOnPageNumberFirstPageListLessThan10Elements(self):
            list = [1,2,3,4,5,6,7,8,9]
            firstPage = ProductLoader.getRangeOfListBaseOnPageNumber(list, 1)
            self.assertEqual(9, len(firstPage)) 
            self.assertEqual(1, firstPage[0]) 
            self.assertEqual(9, firstPage[8]) 

       def testGetRangeOfListBaseOnPageNumberFirstPageListPageZeroReturnsFirstPage(self):
            list = [1,2,3,4,5,6,7,8,9,10,11]
            firstPage = ProductLoader.getRangeOfListBaseOnPageNumber(list, 0)
            self.assertEqual(10, len(firstPage)) 
            self.assertEqual(1, firstPage[0]) 
            self.assertEqual(10, firstPage[9]) 

       def testGetRangeOfListBaseOnPageNumberPageLargerThanNoOfElements(self):
            list = [1,2,3,4,5,6,7,8,9,10,11]
            firstPage = ProductLoader.getRangeOfListBaseOnPageNumber(list, 10)
            self.assertEqual(0, len(firstPage)) 


       def testLoadProductsAndSortByPriceAsc(self):
            sortedProducts = ProductLoader.loadProductsAndSortByPriceAsc()
            self.assertEqual(27, len(sortedProducts)) 
            
            currentMinPrice = sortedProducts[0].price
            for product in sortedProducts:
                   self.assertTrue(product.price >= currentMinPrice, "Sort failed, " + str(product.price) + " greater than " + str(currentMinPrice))
                   currentMinPrice = product.price


       def testProductsKidsOnlySortedByPriceAsc(self):
            sortedProducts = ProductLoader.productsKidsOnlySortedByPriceAsc(1)
            self.assertEqual(10, len(sortedProducts)) 
            
            currentMinPrice = sortedProducts[0].price
            for product in sortedProducts:
                   self.assertTrue(product.price >= currentMinPrice, "Sort failed, " + str(product.price) + " greater than " + str(currentMinPrice))
                   currentMinPrice = product.price
                   
                   self.assertTrue(product.kids, "Ups, product with id " + str(product.id) + " is no kids product")


       def testGetProductById50626(self):
             product = ProductLoader.getProductById(50626)
             self.assertEqual(50626, product.id) 

       def testGetProductByIdUnknownId(self):
             product = ProductLoader.getProductById(0)
             self.assertIsNone(product) 

if __name__ == '__main__':
    unittest.main()
