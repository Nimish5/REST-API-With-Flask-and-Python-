from werkzeug.security import safe_str_cmp
from user import User

# Udemy(REST APIs with Flask and Python): Watch video 71 & 72(Section 4)
# Considering 'u' is the object/ instance that we created in the users list, using User class.
# For better understanding of Classes and Objects, go to: Sololearn.com > OOP(Section 8)

users = [
    User(1, 'Nimish', 'ravimotu'),
    User(8, 'Shubham', 'Jain')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, 'None')
    if user and safe_str_cmp(user.password, password):   # if user and (user.password == password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, 'None')

