from pathlib import Path
path=Path(r"D:\学习文件\GitHub\python-practice\read_file\python_can.txt")
finding=path.read_text().replace('Python','C')
print(finding)

pc_string=finding.splitlines()
print(pc_string)

for string in pc_string:
    print(string)