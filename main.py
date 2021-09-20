import requests
import json
import xml.etree.ElementTree as ET
import xml


class YandexWeather:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        URL = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=3' % (self.lat, self.lon)
        session = requests.Session()
        session.auth = ('X-Yandex-API-Key', ' ')
        response = session.get(URL, headers={'X-Yandex-API-Key': '61e3f1cf-43b8-4b4e-845d-9345fa357b47'})
        s = json.dumps(response.json())
        print(json.loads(s))


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
        print(coords)
        YandexWeather(coordLat, coordLon)

    # @property
    # def getCoordsFromXml(response):
    #     # try:
    #     tree = ET.parse(response)
    #     importSession = tree.getroot()
    #     coords = importSession.find('Envelope')
    #     name = coords[0].attrib
    #     b = name.get('lowerCorner')
    #     print(b)


#
# coords = """response.json()"""
#         print(coords[0])


# server(59.938951, 30.317695)
if __name__ == '__main__':
    YandexMaps('Самара')
    # yandex_weather(59.938951, 30.317695) 37.038186, 'lon': 55.312148


