"""
add an address to zikeshop

$Id$
"""

import zikebase; zikebase.load("ObjectEditor")
import zikeshop
import weblib
weblib.auth.check()

weblib.request.form["customerID"] = weblib.auth.user.ID
ed = zikebase.ObjectEditor(zikeshop.Address)
ed.act()


if weblib.request.get("context") == "checkout":
    assert weblib.request.has_key("whichone"), \
           "checkout context requires a whichone item.."

    cash = zikeshop.Cashier(zikeshop.Cart(), weblib.auth.user)

    #@TODO: clean this up:
    weblib.request.form["action"]="update"
    weblib.request.form[weblib.request["whichone"]+'AddressID'] = ed.object.ID
    cash.act()
    