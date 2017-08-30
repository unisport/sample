#For some reason I can't getting it to run, it runs webservice.py instead.
import unittest
import flask
import webservice

class WebserviceTestCase(unittest.TestCase):
    
    def setUp(self):
        webservice.app.config['TESTING'] = True
        self.app = webservice.app.test_client()
        print 'in setup'
    
    def test_data_access(self):
        """test if webservice.getJsonFromSample() can access the sampledata."""
        dataIsReadable = False
        testdata = self.app.getJsonFromSample()
        try:
            if testdata['end-point'] == '/api/sample/':
                dataIsReadable = True
        except:
            dataIsReadable = False
        self.assertTrue(dataIsReadable)
    
    def test_all_are_kids(self):
        """Test if all products has kids = 1"""
        testdata = loadJson(self.app.get('/products/kids/'))
        allKids = True
        for product in testdata['products']:
            if not product['kids'] == '1':
                allKids = False
                break
        self.assertTrue(allKids)
            
    def test_10_products_returned(self):
        """Test if only 10 products returned if 10 or more is available."""
        testdata = loadJson(self.app.get('/products/'))
        self.assertEqual(len(testdata['products']), 10)
        
    def test_rest_returned(self):
        """test if the reminder of the products is returned if less then 10 remain."""
        testdata = loadJson(self.app.get('/products/?page=3')) # the sampledata only has 25 entries, so ther should be 5 left.
        self.assertEqual(len(testdata['products']), 5)
        
    def test_match_id(self):
        """test if the ID matches the the requested one."""
        testdata = loadJson(self.app.get('/products/157128/'))    # the sampledata contains a product with ID: 157128
        self.assertEquals(testdata['products'][0]['id'], 157128)
        
    def test_sort(self):
        """test if sorted by price, cheapest first."""
        testdata = self.app.getJsonFromSample()
        sortedTestdata = self.app.sortJsonListCheapestFirst(testData)
        isSorted = True
        prev = 0.00    # defaultvalue is zero so is the lowest value, all others range in the above zero.
        for product in sortedTestdata:
            current = float(product['price'].replace(',','.'))
            if not prev < current:
                isSorted = False
                break
            prev = current
        self.assertTrue(isSorted)
        
    def loadJson(jsonStr):
        return json.loads(jsonStr.read())
        
if __name__ == '__main__':
    print 'unittest'
    unittest.main()
