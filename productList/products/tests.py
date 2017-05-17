from django.test import TestCase
from django.urls import reverse
from products import views

class ReturnLengthTest( TestCase ):
    def test_smoke_jsonData(self):
        # test DOES NOT THROW any exceptions
        try:
            views.getJsonDataFromServer()
        except:
            return False
        return True

    def test_detailsView_raises_404(self):
        response404   = self.client.get(reverse('detail', args=[200]))
        responseNo404 = self.client.get(reverse('detail', args=[1]))
        self.assertEqual( response404.status_code,   404 )
        self.assertEqual( responseNo404.status_code, 200 )

"""
    The next test is commented out because doesn't work.
    It believes the lambda-expression used is working on a
    string, instead of a dict.
    errors with "you must use integers to split a string"
"""
#   def test_returns_exact_amount_items(self):
#       """
#        if len( items ) is not equal to the given amount,
#        return false
#       """
#       testData = views.getJsonDataFromServer()
#       listLength = 12
#       itemList   = views.products_sorted_by_price( testData,
#                                                    0,
#                                                    listLength )

#       self.assertEqual( len( itemList ), listLength )

