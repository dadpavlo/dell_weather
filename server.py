from flask import Flask
from flask import request
import json
import numpy
import main

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/weather')
def weather():
    city = request.args.get('city')
    days = request.args.get('days', type=int)
    forecasts = main.get_weather(city, days)
    count_forecasts = count(forecasts, days)

    response = {
        'city': city,
        'from': forecasts[0][0],
        'to': forecasts[days - 1][0],
    }
    response.update(count_forecasts)
    json.dumps(response)
    return response


def count(forecasts, days):
    temperature = []
    humidity = []
    pressure = []

    for i in range(days):
        temperature.append(forecasts[i][1])
        humidity.append(forecasts[i][2])
        pressure.append(forecasts[i][3])

    count_forecasts = {
        'temperature_c': {
            'average': float("{0:.1f}".format(numpy.average(temperature))),
            'median': float("{0:.1f}".format(numpy.median(temperature))),
            'min': float("{0:.1f}".format(numpy.min(temperature))),
            'max': float("{0:.1f}".format(numpy.max(temperature)))
        },
        'humidity': {
            'average': float("{0:.1f}".format(numpy.average(humidity))),
            'median': float("{0:.1f}".format(numpy.median(humidity))),
            'min': float("{0:.1f}".format(numpy.min(humidity))),
            'max': float("{0:.1f}".format(numpy.max(humidity)))
        },
        "pressure_mm": {
            "average": float("{0:.1f}".format(numpy.average(pressure))),
            "median": float("{0:.1f}".format(numpy.median(pressure))),
            "min": float("{0:.1f}".format(numpy.min(pressure))),
            "max": float("{0:.1f}".format(numpy.max(pressure)))
        }
    }

    return count_forecasts


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
