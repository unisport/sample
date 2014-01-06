import unittest
import ModeGetter

class ModeGetterTests(unittest.TestCase):
       def testGetModeProducts(self):
             mode = ModeGetter.getMode("http://workstation.local/wsgi/products/")
             
             self.assertEqual(0, mode)

       def testGetModeProductsNoTraillingSlash(self):
             mode = ModeGetter.getMode("http://workstation.local/wsgi/products")
             
             self.assertEqual(0, mode)

       def testGetModeProductsWithPaging(self):
             mode = ModeGetter.getMode("http://workstation.local/wsgi/products/?page=1")
             
             self.assertEqual(0, mode)

       def testGetModeKids(self):
             mode = ModeGetter.getMode("http://workstation.local/wsgi/products/kids/")
             
             self.assertEqual(1, mode)

       def testGetModeProductById(self):
             mode = ModeGetter.getMode("http://workstation.local/wsgi/products/1234/")
             
             self.assertEqual(2, mode)

       def testGetPageNumberNoNumberPassed(self):
             pageNumber = ModeGetter.getPageNumber("http://workstation.local/wsgi/products/")
             
             self.assertEqual(1, pageNumber)

       def testGetPageNumberOnePassed(self):
             pageNumber = ModeGetter.getPageNumber("http://workstation.local/wsgi/products/?page=1")
             
             self.assertEqual(1, pageNumber)

       def testGetPageNumberZeroPassed(self):
             pageNumber = ModeGetter.getPageNumber("http://workstation.local/wsgi/products/?page=1")
             
             self.assertEqual(1, pageNumber)

       def testGetPageNumberTwoPassed(self):
             pageNumber = ModeGetter.getPageNumber("http://workstation.local/wsgi/products/?page=2")
             
             self.assertEqual(2, pageNumber)

       def testGetProductId(self):
             productId = ModeGetter.getProductId("http://workstation.local/wsgi/products/123/")
             
             self.assertEqual(123, productId)


if __name__ == '__main__':
    unittest.main()
