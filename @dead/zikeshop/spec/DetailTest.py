"""
test cases for zikeshop.Detail
"""
__ver__="$Id$"
import unittest
import zikeshop

class DetailTestCase(unittest.TestCase):

    def check_get_subtotal(self):
        """
        subtotal should always be product price * quantity
        """
        
        det = zikeshop.Detail()
        assert det.subtotal == 0, \
               "wrong default subtotal: %s" % det.subtotal
        
        prod = zikeshop.Product()
        prod.price = '12.00'
        det.product = prod
        assert det.subtotal == 0, \
               "wrong subtotal for 0 quantity: %s" % det.subtotal

        det = zikeshop.Detail()
        det.quantity = 10
        det.product = prod
        assert det.subtotal == 120, \
               "didn't get correct subtotal with nonzero quantity"

        det.quantity = 2
        assert det.subtotal == 24, \
               "didn't change subtotal when quantity changed.."

        
        
    def check_set_subtotal(self):
        det = zikeshop.Detail()
        try:
            gotError = 0
            det.subtotal = 5
        except TypeError:
            gotError = 1
        assert gotError, \
               "shouldn't be able to assign to detail.subtotal"