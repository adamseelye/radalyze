import bcrypt

class hashedPassword:
    def hash_func(password):

        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()

        hash = bcrypt.hashpw(bytes, salt)

        return hash

    def check_func(user_pwd, hashed):
        
        user_bytes = user_pwd.encode('utf-8')

        result = bcrypt.checkpw(user_bytes, hashed)

        return result
