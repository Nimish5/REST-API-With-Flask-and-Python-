from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.search_by_username(username)
    if user and safe_str_cmp(user.password, password):   # if user and (user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.search_by_id(user_id)

