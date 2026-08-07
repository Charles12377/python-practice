name1='Eric'
message=f'hello {name1},would you like to learn some Python today?'
print(message)
print(name1.title())
print(name1.upper())
print(name1.lower())

famous_name='Albert Einstin'
famous_quote='A person who never made a mistake never tried anything new.'
message=f'{famous_name} once said,"{famous_quote}"'
print(message)

name2='\tcharle\n'
print(name2)
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

filename='python_notes.txt'
print(filename.removesuffix('.txt'))