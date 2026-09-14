from test.city_functions import city_country

def test_city_country():
    message=city_country('tianjin','china')
    assert message == 'Tianjin,China'