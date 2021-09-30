# How it works
Enter:\
```/weather?city=<city>&days=<n>```

Where **_city_** is any city or place, and **_n_** is the number of days for the forecast (less than 7).\
Get a response in json format containing the average, median, maximum and minimum values of the temperature, humidity and pressure parameters.

# For example
Enter:\
```/weather?city=Самара&days=3```\
Get response: 
``` 
{
    "city": "Самара",
    "from": "2021-09-21",
    "humidity": {
        "average": 72.3,
        "max": 82.0,
        "median": 74.0,
        "min": 61.0
    },
    "pressure_mm": {
        "average": 758.3,
        "max": 760.0,
        "median": 759.0,
        "min": 756.0
    },
    "temperature_c": {
        "average": 11.7,
        "max": 12.0,
        "median": 12.0,
        "min": 11.0
    },
    "to": "2021-09-23"
}
```
# Docker
Start on local Linux machine \
docker build [PATH_TO_DOCKERFILE] -t dell-weather \
docker run -p 8080:8080 dell-weather

# API KEY
Create file config.ini and requests keys from the developer
