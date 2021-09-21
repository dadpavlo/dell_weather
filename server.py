from flask import Flask
from flask import request
import requests
import json
import numpy

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/weather')
def weather():
    city = request.args.get('city')
    days = request.args.get('days', type=int)
    URL = 'https://geocode-maps.yandex.ru/1.x/?geocode=%s' % (city)
    session = requests.Session()
    response = session.get(
        'https://geocode-maps.yandex.ru/1.x/?apikey=0295000a-c2ac-4bce-8cee-4ed89f877a4d&geocode=%s&format=json' % city)
    coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    coords = json.dumps(coords)
    coords = json.loads(coords)
    coordLon = coords.split()[0]
    coordLat = coords.split()[1]
    URL = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=%s' % (coordLat, coordLon, days)
    session = requests.Session()
    session.auth = ('X-Yandex-API-Key', ' ')
    response = session.get(URL, headers={'X-Yandex-API-Key': '61e3f1cf-43b8-4b4e-845d-9345fa357b47'})
    response = json.dumps(response.json())
    response = json.loads(response)
    temp = dict()
    for i in range(days):
        data = list()
        data.append(response['forecasts'][i]['date'])
        data.append(response['forecasts'][i]['parts']['day']['temp_avg'])
        data.append(response['forecasts'][i]['parts']['day']['humidity'])
        data.append(response['forecasts'][i]['parts']['day']['pressure_mm'])
        temp.update({i: data})
        data = []
    temperature = []
    hummidity = []
    pressure = []
    for i in range(days):
        temperature.append(temp[i][1])
        hummidity.append(temp[i][2])
        pressure.append(temp[i][3])
    print(temperature)
    temperature_avg = numpy.average(temperature)
    temperature_med = numpy.median(temperature)
    temperature_max = numpy.max(temperature)
    temperature_min = numpy.min(temperature)

    hummidity_avg = numpy.average(hummidity)
    hummidity_med = numpy.median(hummidity)
    hummidity_max = numpy.max(hummidity)
    hummidity_min = numpy.min(hummidity)

    pressure_avg = numpy.average(pressure)
    pressure_med = numpy.median(pressure)
    pressure_max = numpy.max(pressure)
    pressure_min = numpy.min(pressure)

    res = {
        'city': city,
        'from': str(temp[0][0]),
        'to': str(temp[days-1][0]),
        'temperature_c': {
            'average': float(temperature_avg),
            'median': float(temperature_med),
            'min': float(temperature_min),
            'max': float(temperature_max)
            },
        'humidity': {
            'average': float(hummidity_avg),
            'median': float(hummidity_med),
            'min': float(hummidity_max),
            'max': float(hummidity_min)
        },
        "pressure_mb": {
            "average": float(pressure_avg),
            "median": float(pressure_med),
            "min": float(pressure_max),
            "max": float(pressure_min)
        }
    }

    print(type(res))
    json.dumps(res)
    return res

# def get_weather(lat, lon, days):
#     URL = 'https://api.weather.yandex.ru/v2/forecast?lat=%s&lon=%s&limit=%s' % (lat, lon, days)
#     session = requests.Session()
#     session.auth = ('X-Yandex-API-Key', ' ')
#     response = session.get(URL, headers={'X-Yandex-API-Key': '61e3f1cf-43b8-4b4e-845d-9345fa357b47'})
#     response = json.dumps(response.json())
#     response = json.loads(response)
#     temp = dict()
#     for i in range(days):
#         data = list()
#         data.append(response['forecasts'][i]['parts']['day']['temp_avg'])
#         data.append(response['forecasts'][i]['parts']['day']['humidity'])
#         data.append(response['forecasts'][i]['parts']['day']['pressure_mm'])
#         temp.update({response['forecasts'][i]['date']: data})
#         data = []
#     return temp['2021-09-21']
#
#
# def get_coords(place, days):
#     URL = 'https://geocode-maps.yandex.ru/1.x/?geocode=%s' % (place)
#     session = requests.Session()
#     response = session.get(
#         'https://geocode-maps.yandex.ru/1.x/?apikey=0295000a-c2ac-4bce-8cee-4ed89f877a4d&geocode=%s&format=json' % place)
#     coords = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
#     coords = json.dumps(coords)
#     coords = json.loads(coords)
#     coordLat = coords.split()[0]
#     coordLon = coords.split()[1]
#     get_weather(coordLon, coordLat, days)


if __name__ == "__main__":
    app.run()
