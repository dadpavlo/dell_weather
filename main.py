import requests
import json
import configparser

def get_api_keys():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_weather(place, days):
    API_KEY = get_api_keys()
    URL_YANDEXMAPS = (
            'https://geocode-maps.yandex.ru/1.x/?apikey=%s&geocode=%s&format=json' % (API_KEY['api_keys']['maps_api_key'], place))
    session = requests.Session()
    response = session.get(URL_YANDEXMAPS)
    coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coords = json.dumps(coords)
    coords = json.loads(coords)
    coord_lat = coords.split()[0]
    coord_lon = coords.split()[1]

    URL_YANDEXWEATHER = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=%s' % (
    coord_lon, coord_lat, days)
    session = requests.Session()
    session.auth = ('X-Yandex-API-Key', ' ')
    response = session.get(URL_YANDEXWEATHER, headers={'X-Yandex-API-Key': API_KEY['api_keys']['weather_api_key']})
    response = json.dumps(response.json())
    response = json.loads(response)
    forecasts = dict()
    for i in range(days):
        data = list()
        data.append(response['forecasts'][i]['date'])
        data.append(response['forecasts'][i]['parts']['day']['temp_avg'])
        data.append(response['forecasts'][i]['parts']['day']['humidity'])
        data.append(response['forecasts'][i]['parts']['day']['pressure_mm'])
        forecasts.update({i: data})
        data = []
    return forecasts
