from pathlib import Path 
path = Path('D:/学习文件/GitHub/python-practice/read_file/pi_digits.txt') 
contents = path.read_text() 
print(contents)
