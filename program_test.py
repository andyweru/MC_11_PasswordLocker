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

if __name__ == '__main__':
    unittest.main()
        