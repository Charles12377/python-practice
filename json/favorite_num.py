from pathlib import Path
import json

def get_stored_num(path):
    """如果已经存储就获取数字"""
    if path.exists():
        contents=path.read_text()
        favorite_num=json.loads(contents)
        return favorite_num
    else:
        return None

def get_new_num(path):
    """提示用户写入数字并存储"""
    favorite_num=input("Enter your favorite number:")
    contents=json.dumps(favorite_num)
    path.write_text(contents)
    return favorite_num

def greet():
    """向用户输出"""
    path=Path(r"D:\学习文件\GitHub\python-practice\json\favorite_num.json")
    favorite_num=get_stored_num(path)
    if favorite_num:
        print(f"I know your favorite number!It's {favorite_num}")
    else:
        favorite_num=get_new_num(path)
        print(f"I know your favorite number!It's {favorite_num}")

greet()