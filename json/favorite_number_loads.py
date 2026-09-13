from pathlib import Path
import json

path=Path(r"D:\学习文件\GitHub\python-practice\json\favorite_number.json")
contents=path.read_text()
message=json.loads(contents)
print(f"I know your favorite number!It's {message}")