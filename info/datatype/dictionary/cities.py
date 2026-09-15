cities={
    '北京':{
        'country':'China',
        'population':2000,
        'fact':'首都',
        },
    'New York':{
        'country':'American',
        'population':1500,
        'fact':'economic centre',
        },

    'London':{
        'country':'Eligland',
        'population':700,
        'fact':'capital',
        },    
    }
for city,info in cities.items():
    print(f"This is {city}:\n\t{info}")