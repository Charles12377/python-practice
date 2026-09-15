from pathlib import Path

names=""
path=Path(r"D:\学习文件\GitHub\python-practice\file\write_file\guest_book.txt")
while True:
    name=input("Please enter your name:(Enter q will quit)")
    if name != 'q':
        names += name+'\n'
    else:
        break

path.write_text(names)

    