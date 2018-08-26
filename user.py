class User:
    """ Class Generates new instances of Users """

    Users = [] #list of users

    username = ''
    email = ''
    password = ''

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def add_user(self):

        """ save_contact method saves contact objects into contact_list """

        User.Users.append(self)
    

