class Report:

    def show(self, model={}):
        print self.fetch(model)

    def fetch(self, model={}):
        import copy   # used by scope
        self.model = model
        scope = model
        scope_stack = []
        zres = ""
        import tpl_sslhead
        zres = zres+ tpl_sslhead.fetch(scope)
        zres = zres + '<'
        zres = zres + 'h1'
        zres = zres + '>'
        zres = zres + str(scope.get('message',''))
        zres = zres + '<'
        zres = zres + '/h1'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'h3'
        zres = zres + '>'
        zres = zres + 'You may enter existing account info:'
        zres = zres + '<'
        zres = zres + '/h3'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'form action=\"'
        zres = zres + str(scope.get('action',''))
        zres = zres + '\" method=\"post\"'
        zres = zres + '>'
        zres = zres + str(scope.get('hidden',''))
        zres = zres + '<'
        zres = zres + 'table border=\"0\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + 'email:'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"text\" name=\"auth_email\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + 'password'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"password\" name=\"auth_password\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td colspan=\"2\" align=\"right\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"submit\" value=\"log in\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td colspan=\"2\" align=\"right\"'
        zres = zres + '>'
        zres = zres + '['
        zres = zres + '<'
        zres = zres + 'a href=\"password.py\"'
        zres = zres + '>'
        zres = zres + 'forgot your password?'
        zres = zres + '<'
        zres = zres + '/a'
        zres = zres + '>'
        zres = zres + ']'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/table'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/form'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'h3'
        zres = zres + '>'
        zres = zres + '...or create a new account:'
        zres = zres + '<'
        zres = zres + '/h3'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'form action=\"newcustomer.py\" method=\"post\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'table border=\"0\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + 'email:'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"text\" name=\"email\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'tr'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + 'password'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"password\" name=\"password\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/td'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/tr'
        zres = zres + '>'
        import tpl_address
        zres = zres+ tpl_address.fetch(scope)
        zres = zres + '<'
        zres = zres + '/table'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"hidden\" name=\"isPrimary\" value=\"1\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/form'
        zres = zres + '>'
        import tpl_sslfoot
        zres = zres+ tpl_sslfoot.fetch(scope)
# end of Report.fetch()
        return zres

def fetch(model={}):
    return Report().fetch(model)
    
def show(model={}):
    return Report().show(model)