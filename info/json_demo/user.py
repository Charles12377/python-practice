from pathlib import Path 
import json 

def get_stored_username(path):
    """如果存储了用户名，就获取它""" 
    if path.exists(): 
        contents = path.read_text() 
        user = json.loads(contents) 
        return user
    else:
        return None 

def get_new_username(path): 
    """提示用户输入用户名""" 
    username = input("What is your name? ") 
    usersex=input("Sex:")
    userage=input("Age:")
    user={'name':username,
          'sex':usersex,
          'age':userage,
          }
    contents = json.dumps(user) 
    path.write_text(contents) 
    return user 
 
def greet_user(): 
    """问候用户，并指出其名字""" 
    path = Path(r'D:\学习文件\GitHub\python-practice\json\user.json') 
    user = get_stored_username(path)
    verify=input(f"Are you {user['name']}? (Yes or No)")
    if verify.lower() == 'yes': 
        print(f"Welcome back, {user['name']}!") 
    else: 
        user = get_new_username(path) 
        print(f"We'll remember you when you come back, {user}!") 
 
greet_user()