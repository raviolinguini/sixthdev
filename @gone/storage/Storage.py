
class Storage:

    def store(self, table, **row):
        if row.get("ID"):
            return self._update(table, **row)
        else:
            return self._insert(table, **row)

    def fetch(self, table, ID):
        res = self.match(table, ID=ID)
        assert len(res)==1, "fetch() should return 1 row. got %i" % len(res)
        return res[0]


    ## abstract:

    def delete(self, table, ID):
        raise NotImplementedError
        
    def match(self, table, **where):
        raise NotImplementedError
    
    def _insert(self, table, **row):
        raise NotImplementedError

    def _update(self, table, **row):
        raise NotImplementedError