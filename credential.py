class Credential:
    """ Class Generates new instances of account credentials """

    Accounts = []

    platform = ''
    platform_username = ''
    platform_password = ''

    def __init__(self, platform, username, password):
        self.platform = platform
        self.platform_username = username
        self.platform_password = password
    

    def add_credentials(self):
        """ save new credentials to Accounts List """

        Credential.Accounts.append(self)
