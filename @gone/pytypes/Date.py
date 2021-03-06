"""
zdc.Date stuff
"""
__ver__="$Id$"

import calendar
import copy
import time
from DateTime import DateTime

class Date(DateTime):
    """
    A class to represent dates.
    """
    def __init__(self, datestr):
        """
        Construct a Date from a string representation.
        """
        DateTime.__init__(self, datestr)
        self.hh = self.mm = self.ss = 0

    def toSQL(self):
        res = "%i-%i-%i" % (self.y, self.m, self.d)
        if res =="0-0-0":
            return ''
        else:
            return res

    def toUS(self):
        return "%02i/%02i/%04i" % (self.m, self.d, self.y)        

##     def __cmp__(self, other):
##         if isinstance(other, Date):
##             return cmp([self.y, self.m, self.d], [other.y, other.m, other.d])
##         elif isinstance(other, DateTime):
##             # NOTE: uses arcane DateTime knowledge.
##             # Originally coded as
##             #    return cmp(other, self)*-1
##             return cmp([self.y, self.m, self.d, 0, 0, 0],
##                        [other.y, other.m, other.d,
##                         other.hh, other.mm, other.ss])
##         else:
##             return cmp(self, Date(other))

    def __str__(self):
        return self.toSQL()

    def __repr__(self):
        return "Date('%s')" % self.toUS()
