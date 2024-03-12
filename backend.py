"""
This is the backend that controls the database for the hashed passwords as well as the master hashed password


Created by Caleb 
"""

# These are subject to change, please refer to requirements.txt
import string
import random
import hashlib
import sqlite3

class PasswordGenerator:
    def __init__(self, length, special='n', digits='y', purpose=''):
        self.length = length
        self.special = special
        self.digits = digits
        self.purpose = purpose

    def generate_password(self):
        if self.length < 8:
            raise ValueError('Password length must be at least 8 characters')

        char_pools = {
            'lower': string.ascii_lowercase,
            'upper': string.ascii_uppercase,
            'digits': string.digits if self.digits == 'y' else '',
            'special': string.punctuation if self.special == 'y' else ''
        }

        password_chars = [random.choice(char_pools[key]) for key in char_pools if char_pools[key]]

        combined_pool = ''.join(char_pools.values())
        password_chars.extend(random.choices(combined_pool, k=self.length - len(password_chars)))

        random.shuffle(password_chars)

        return ''.join(password_chars)
