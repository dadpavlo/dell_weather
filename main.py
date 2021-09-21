import requests
import json
import server


def get_weather(lat, lon, days):
    URL = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=%s' % (lat, lon, days)
    session = requests.Session()
    session.auth = ('X-Yandex-API-Key', ' ')
    response = session.get(URL, headers={'X-Yandex-API-Key': '61e3f1cf-43b8-4b4e-845d-9345fa357b47'})
    response = json.dumps(response.json())
    response = json.loads(response)
    temp = dict()
    for i in range(days):
        data = list()
        data.append(response['forecasts'][i]['parts']['day']['temp_avg'])
        data.append(response['forecasts'][i]['parts']['day']['humidity'])
        data.append(response['forecasts'][i]['parts']['day']['pressure_mm'])
        temp.update({response['forecasts'][i]['date']: data})
        data = []
    return str(temp)


def get_coords(place, days):
    URL = 'https://geocode-maps.yandex.ru/1.x/?geocode=%s' % (place)
    session = requests.Session()
    response = session.get(
        'https://geocode-maps.yandex.ru/1.x/?apikey=0295000a-c2ac-4bce-8cee-4ed89f877a4d&geocode=%s&format=json' % place)
    coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coords = json.dumps(coords)
    coords = json.loads(coords)
    coordLat = coords.split()[0]
    coordLon = coords.split()[1]
    get_weather(coordLon, coordLat, days)


if __name__ == '__main__':
    server.app.run()
