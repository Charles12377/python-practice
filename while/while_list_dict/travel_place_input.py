travel_places={}
will=True
while will == True:
    name=input("What's your name?")
    place=input("If you could visit one place in the world,"
                "where would you go?")
    travel_places[name]=place
    intention=input("Whether to continue?(Yes/No)")
    if intention == 'No':
        will=False
for Name,Place in travel_places.items():
    print(f"{Name} want to {Place}.")




