"""
App to let users signup, login, request passwords, etc.
"""
__ver__="$Id$"

import zikebase
zikebase.load("AppActor")

class UserApp(zikebase.AppActor):

    def act_create(self):

        # create the user:
        ed = zikebase.ObjectEditor(zikebase.User, input=self.input)
        ed.do("save")