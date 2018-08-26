from credential import Credential

class User:
    """ Class Generates new instances of Users """

    Users = [] #list of users

    username = ''
    email = ''
    password = ''

    Accounts = []

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def add_user(self):

        """ save_contact method saves contact objects into contact_list """

        User.Users.append(self)

    @classmethod
    def find_user(cls,persona,secret):
        '''
        Method that takes in a persona and returns a user that matches that persona.

        Args:
            persona: Person to search for
        Returns :
            details of person that matches the persona.
        '''

        for saved_user in cls.Users:
            if saved_user.username == persona and saved_user.password == secret:
                return saved_user
    

