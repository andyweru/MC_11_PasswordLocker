import unittest
from user import User
from credential import Credential

class TestProgram(unittest.TestCase):
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

    def test_save_multiple_contact(self):
            ''' test whether multiple users can be stored'''
            self.new_user.add_user()
            other_user= User("Gucci","gucci@gmail.com","password456") # new user
            other_user.add_user()
            self.assertEqual(len(User.Users),2)

    def test_find_user(self):
        ''' test whether user can be found by username and password'''

        self.new_user.add_user()
        other_user = User("Gucci","gucci@gmail.com", "password456") # new contact
        other_user.add_user()

        retrieved_user = User.find_user("Gucci", "password456")

        self.assertEqual(retrieved_user.username,other_user.username)

if __name__ == '__main__':
    unittest.main()
        