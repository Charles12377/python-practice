def city_country(city,country):
    citycountry=f"{city},{country}"
    return citycountry.title()
message=city_country('杭州','中国')
print(message)
message=city_country('兰州','中国')
print(message)
message=city_country('new york','american')
print(message)