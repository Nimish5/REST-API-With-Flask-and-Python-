from user import User
# from werkzeug.security import safe_str_cmp

Existing_User = [
   User(6, 'Shubham', 'Jain08'),
   User(5, 'Nimish', 'sexynimish07'),
   User(4, 'Hemlata', 'Mummy')
]

username_mapping = {u.username: u for u in Existing_User}
userid_mapping = {u.id: u for u in Existing_User}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:    # if user and safe_str_cmp(user.password, password)
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)