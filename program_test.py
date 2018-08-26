import unittest
from user import User
from credential import Credential

class TestUser(unittest.TestCase):
    """ Test class for defining test cases for program behaviors """

    def setUp(self):
        """ Runs before each test case """

        self.new_user = User("YoungWeshy",  "andyweru@gmail.com", "password123")

    def tearDown(self):
        """ Runs after every test case """

        User.Users = []

    def test_init(self):
        """ Test whether object is initialized properly """

        self.assertEqual(self.new_user.username,"YoungWeshy")
        self.assertEqual(self.new_user.email,"andyweru@gmail.com")
        self.assertEqual(self.new_user.password,"password123")

    def test_add_user(self):
        """ test whether new user is added to Users list """

        self.new_user.add_user()

        self.assertEqual(len(User.Users), 1)

    def test_save_multiple_users(self):
            ''' test whether multiple users can be stored'''

            self.new_user.add_user()
            other_user= User("Gucci","gucci@gmail.com","password456")
            other_user.add_user()
            self.assertEqual(len(User.Users),2)

    def test_find_user(self):
        ''' test whether user can be found by username and password'''

        self.new_user.add_user()
        other_user = User("Gucci","gucci@gmail.com", "password456") # new contact
        other_user.add_user()

        retrieved_user = User.find_user("Gucci", "password456")

        self.assertEqual(retrieved_user.username,other_user.username)



class TestCredential(unittest.TestCase):
    """ Test class for defining test cases for credential behavior """

    def setUp(self):
        """runs before each credential test case"""

        self.new_credential = Credential("Twitch", "youngWeshy", "password123")

    def tearDown(self):
        """ Runs after each credential test case"""

        Credential.Accounts = []

    def test_init(self):
        """ Test whether credential objects are initialized properly """

        self.assertEqual(self.new_credential.platform, "Twitch")
        self.assertEqual(self.new_credential.platform_username, "youngWeshy")
        self.assertEqual(self.new_credential.platform_password, "password123")

    def test_add_credentials(self):
        """ test whether new credential is added to Accounts list """

        self.new_credential.add_credentials()

        self.assertEqual(len(Credential.Accounts), 1)

    def test_save_multiple_credentials(self):
        """ test whether multiple users can be stored """

        self.new_credential.add_credentials()
        other_credential= Credential("Twitter", "Wesh", "password123")
        other_credential.add_credentials()
        self.assertEqual(len(Credential.Accounts),2)

    def test_find_credential(self):
        """ test whether credential can be found by platform """

        self.new_credential.add_credentials()
        other_credential = Credential("Twitter", "Wesh", "password123")

        other_credential.add_credentials()

        retrieved_credential = Credential.find_credential("Twitter")

        self.assertEqual(retrieved_credential.platform, other_credential.platform)



if __name__ == '__main__':
    unittest.main()
        