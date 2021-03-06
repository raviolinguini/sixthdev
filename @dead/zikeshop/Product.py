"""
Product.py - product object for zikeshop
"""
__ver__="$Id$"

from zikeshop import Picture
from pytypes import FixedPoint
from strongbox import *

class Product(Strongbox):
    ID = attr(long)
    _pic = attr(Picture)
    code = attr(str)
    name = attr(str)
    brief = attr(str)
    descript = attr(str)
    warn = attr(int, okay=[0,1], default=0)
    price = attr(FixedPoint, default=0)
    cost = attr(FixedPoint, default=0)
    retail = attr(FixedPoint, default=0)
    weight = attr(FixedPoint, default=0)
    isHidden = attr(int, okay=[0,1], default=0)
    hold = attr(int) # @TODO: what does this mean again?
    stock = attr(int, default=-1) # no value known
    warn = attr(int, default=-1)  # no warning amount
    
    #_tuples = ['styles', 'categories']
    #self._data['class'] = "product"
    #self.parentID = 0


    def delete(self):
        self.categories.delete()
        #@TODO: clean this up:
        for style in self.styles:
            style.delete()
        super(Product,self).delete()


## @TODO: move duplicate code check to admin app or something.
## # check for dulplicate codes:
##         where = "code = '%s'" % (self.code)
##         if self.ID:
##             where = where + "AND ID != %i" % int(self.ID)
##         if self._ds.select(self._tablename, where):
##             raise ValueError, "This code already exists!"


    def get_available(self):
        #@TODO: this is where styled/unstyled distinction
        # would come in handy
        res = (self.stock or 0) - self.hold
        for item in self.styles:
            res = res + (item.stock or 0) - item.hold
        return res
    

##     #@TODO: proper linkset for product styles
##     def get_styles(self):
##         if not self._data.has_key("_styles"):
##             self._data["_styles"] = LinkSet(self,
##                                                 zikeshop.Style,
##                                                 "parentID")
##         return self._data["_styles"]

    ## @TODO: category junction stuff ############################

##     def get_categories(self):
##         if not self._data.has_key("cats"):
##             self._data["cats"] = Junction(self,
##                                               zikeshop.Category,
##                                               "shop_product_node",
##                                               "productID", "nodeID")
##         return self._data["cats"]
          
##     def set_categories(self, value):
##         vals = []
##         if type(value) == type(0):
##             vals.append(value)
##         elif type(value)==type(""):
##             vals.append(int(value))
##         elif type(value) in (type(()), type([])):
##             for item in value:
##                 vals.append(int(item))
##         else:
##             raise TypeError, \
##                   "value assigned to categories should be int or int list," \
##                   "not %s" % type(value)

##         self.categories.clear()
##         from zikeshop import Category
##         for catID in vals:
##             self.categories << Category(self._ds, "@TODO: fixme!", ID=catID)

