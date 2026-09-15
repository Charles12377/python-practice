from pathlib import Path

name=input("Please enter your name:")
path=Path(r"D:\学习文件\GitHub\python-practice\file\write_file\guest.txt")
path.write_text(name)