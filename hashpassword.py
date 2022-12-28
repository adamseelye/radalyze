# This class is used both for hashing a user's password
# to be uploaded to the database or to check if a
# given password matches a hash

import bcrypt

class hashedPassword:
    def hash_func(password):

        bytes = password.encode('utf-8')    # UTF-8 byte encode password
        salt = bcrypt.gensalt()     # Generate salt for better security
        hash = bcrypt.hashpw(bytes, salt)   # Full hash is bytes + salt

        return hash                 

    def check_func(user_pwd, hashed):
        
        user_bytes = user_pwd.encode('utf-8')
        result = bcrypt.checkpw(user_bytes, hashed)

        return result

