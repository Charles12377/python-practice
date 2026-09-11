from pathlib import Path 
path = Path(r'D:\学习文件\GitHub\python-practice\read_file\pi_digits.txt') 
contents = path.read_text() 
lines = contents.splitlines() 
pi_string = '' 
for line in lines: 
    pi_string += line.strip() 

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string: 
    print("Your birthday appears in the first million digits of pi!")
else: 
    print("Your birthday does not appear in the first million digits of pi.")

