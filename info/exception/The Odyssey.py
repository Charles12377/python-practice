from pathlib import Path

path=Path(r"D:\学习文件\GitHub\python-practice\exception\The Odyssey .txt")
messages=path.read_text(encoding='utf-8').split()
print(messages.count('loves'))
