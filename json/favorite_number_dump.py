from pathlib import Path
import json

path=Path(r"D:\学习文件\GitHub\python-practice\json\favorite_number.json")
favorite_num=input("Enter your favorite number:")
contents=json.dumps(favorite_num)
path.write_text(contents)