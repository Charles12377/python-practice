from pathlib import Path

paths=[r"D:\学习文件\GitHub\python-practice\exception\dogs.txt",
       r"D:\学习文件\GitHub\python-practice\exception\cats.txt"]
for path in paths:
    try:
        messages=Path(path)
        content=messages.read_text(encoding='utf-8')
        print(content)
    except FileNotFoundError:
        pass
        #print("The file can't find out.")