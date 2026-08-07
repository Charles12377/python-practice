name='ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

first_name='ada'
last_name='lovelace'
full_name=f'{first_name} {last_name}'
message=f'hello,{full_name}'.title()
print(message)

language=' python '
language=language.strip()
print(language)

starch_url='http://nostarch.com'
simple_url=starch_url.removeprefix('http://')
print(simple_url)