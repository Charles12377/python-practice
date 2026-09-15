favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'rust', 
    'phil': 'python', 
    } 
for name, language in favorite_languages.items(): 
    print(f"{name.title()}'s favorite language is \
{language.title()}.")

peoples=['John','Jordan','Sarah','Phil']
for people in peoples:
    if people.lower() in favorite_languages.keys():
        print(f'{people.title()},thank you join the survey.')
    else:
        print(f'{people.title()},please join the survey.')