from .city_functions import city_country

def test_city_country():
    message=city_country('tianjin','china')
    assert message == 'Tianjin,China'

def test_city_country_population():
    message=city_country('tianjin','china','10000000')
    assert message == 'Tianjin,China-Population 10000000'
