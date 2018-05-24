class User:
    def __init__(self, user_id, email=None, password=None,
                 authenticated=False):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.authenticated = authenticated

    def __repr__(self):
        r = {
            'user_id': self.user_id,
            'email': self.email,
            'password': self.password,
            'authenticated': self.authenticated,
        }
        return str(r)

    def can_login(self, password):
        return self.password == password

    def is_active(self):
        return True

    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False