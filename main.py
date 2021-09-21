import requests
import json


class YandexWeather:

    def __init__(self, lat, lon, days):
        self.lat = lat
        self.lon = lon
        self.days = days
        URL = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=%s' % (self.lat, self.lon, self.days)
        session = requests.Session()
        session.auth = ('X-Yandex-API-Key', ' ')
        response = session.get(URL, headers={'X-Yandex-API-Key': '61e3f1cf-43b8-4b4e-845d-9345fa357b47'})
        s = json.dumps(response.json())
        s = json.loads(s)
        temp = dict()
        for i in range(self.days):
            data = list()
            data.append(s['forecasts'][i]['parts']['day']['temp_avg'])
            data.append(s['forecasts'][i]['parts']['day']['humidity'])
            data.append(s['forecasts'][i]['parts']['day']['pressure_mm'])
            temp.update({s['forecasts'][i]['date']: data})
            data = []
        print(temp)



class YandexMaps:

    def __init__(self, place):
        self.place = place
        URL = 'https://geocode-maps.yandex.ru/1.x/?geocode=%s' % (self.place)
        session = requests.Session()
        response = session.get('https://geocode-maps.yandex.ru/1.x/?apikey=0295000a-c2ac-4bce-8cee-4ed89f877a4d&geocode=%s&format=json' % place)
        coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        coords = json.dumps(coords)
        coords = json.loads(coords)
        coordLat = coords.split()[0]
        coordLon = coords.split()[1]
        YandexWeather(coordLon, coordLat, 3)

if __name__ == '__main__':
    YandexMaps('Нью-Йорк')

