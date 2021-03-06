"""
fake data for testing Zikeshop
"""
__ver__="$Id$"

import sixthday
import zikeshop
from sixthday import User
import zdc


def load():
    from zikeshop.test import dbc

    ## clear out old data..
    dbc.delete("base_contact")
    dbc.delete("base_user")
    dbc.delete("base_node")
    dbc.delete("shop_product")
    dbc.delete("shop_card")
    dbc.delete("shop_sale")
    dbc.delete("shop_detail")
    dbc.delete("shop_product_node")

    user = User(dbc)
    user.username=user.uid="username"
    user.email="user@schmoop.com"
    user.password="password"
    user.save()

    user = User(dbc)
    user.username=user.uid=user.email="michal@sabren.com"
    user.password="michal"
    user.save()

    nodeIDs={}
    for n in ("toys", "books", "electronics", "games"):
        node = sixthday.Node(dbc)
        node.descript=""
        node.name=n
        if n=="games":
            node.parentID=nodeIDs["toys"]
        node.save()
        nodeIDs[n] = node.ID


    ## PRODUCTS#################################

    for p in (("DIC00", "dictionary", "defines words", ("books",)),
              ("GUN00", "ray gun", "shoots people", ("toys","electronics")),
              ("GAM00", "monopoly", "get rich quick", ("games",)),
              ("GAM01", "candyland", "an old game", ("games",)),
              ("GAM02", "chess", "an ancient game", ("games",)),
              ("PDA00", "palm pilot", "stores stuff", ("electronics",))):

        prod = zikeshop.Product(dbc)
        prod.code=p[0]
        prod.name=p[1]
        prod.price=5.00 # everything's five bucks!
        prod.descript=p[2]
        #if len(p)>4:
        #    prod.pictureID = p[4]
        prod.categories=map(nodeIDs.get, p[3])
        prod.save()

        ## set up 10 of each product in inventory..
        if prod.name == "dictionary":
            # dictionary has two styles:
            style = zikeshop.Style(dbc)
            #@TODO: clean up this linking bit (use prod.styles << )
            style.parentID = prod.ID
            style.code = "DICTWEB"
            style.name = "Websters"
            style.save()

            style = zikeshop.Style(dbc)
            style.code = "DICTOXF"
            style.name = "Oxford"
            style.parentID=prod.ID
            style.save()
            
        else:
            pass
            # everything else has only one style:
##             style = zikeshop.Style(productID=prod.ID)
##             dbc.cursor().execute("INSERT INTO shop_inventory "
##                                  "(locationID, styleID, amount) "
##                                  "VALUES (1, %i, 10)" % style.ID)


    ## SALES #######################
    sale = zikeshop.Sale(dbc)
    det = zikeshop.Detail(dbc)
    det.productID = zikeshop.Product(dbc, code="GAM02").ID # chess
    sale.status = "new"
    sale.details << det
    sale.save()

if __name__=="__main__":
    load()
