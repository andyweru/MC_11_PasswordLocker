#!/usr/bin/env python3.6
from user import User
from credential import Credential

def create_user(username, email, password):
    ''' Function to create a new user '''
    new_user= User(username, email, password)
    return new_user

def create_credential(platform, platform_username, platform_password):
    ''' Function to create a new credential '''
    new_credential = Credential(platform, platform_username, platform_password)
    return new_credential

def save_User(user):
    ''' Function to save use '''
    user.add_user()

def save_Credential(credential):
    ''' Function to save use '''
    credential.add_credentials()

def find_user(persona, secret):
    ''' Function that finds a user by persona and returns the user '''
    return Contact.user(persona, secret)

def find_credential(network):
    ''' Function that finds a credential in list '''
    return Credential.find_credential(network)

def display_users():
    ''' Function that returns all the saved users '''
    return Contact.display_users()

def display_credentials():
    ''' Function that returns all the saved users '''
    return Credential.display_credentials()  