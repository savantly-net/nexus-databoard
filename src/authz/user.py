
class User (object):
    def __init__ (self, username, roles):
        self.username = username
        self.roles = roles

    def __repr__ (self):
        return '<User %r>' % self.username

    def __eq__ (self, other):
        return self.username == other.username

    def __ne__ (self, other):
        return not self.__eq__ (other)

    def has_role (self, role):
        return role in self.roles

    def is_admin (self):
        return self.has_role ('ADMIN')

    def is_authenticated (self):
        return True

    def is_active (self):
        return True

    def is_anonymous (self):
        return False

    def get_id (self):
        return self.username