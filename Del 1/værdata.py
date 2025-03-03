import datetime as dt

vaerdata = {
  "lat":59.97,"lon":10.78,"timezone":"Europe/Oslo","timezone_offset":7200,"daily": [
    { 
      "dt":1649329200,
      "sunrise":1649305463,
      "sunset":1649355199,
      "moonrise":1649311440,
      "moonset":1649295060,
      "moon_phase":0.19,
      "temp":{"day":277.51,"min":271.29,"max":277.51,"night":271.8,"eve":273.29,"morn":271.79},
      "feels_like":{"day":273.59,"night":265.92,"eve":268.02,"morn":269.78},
      "pressure":956,
      "humidity":46,
      "dew_point":267.62,
      "wind_speed":6.13,
      "wind_deg":19,
      "wind_gust":13.63,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.89,"snow":1.65,"uvi":1.57
    },
    {
      "dt":1649415600,
      "sunrise":1649391683,
      "sunset":1649441745,
      "moonrise":1649400060,
      "moonset":1649385480,
      "moon_phase":0.22,
      "temp":{"day":274.79,"min":270.59,"max":275.91,"night":271.85,"eve":274.38,"morn":270.83},
      "feels_like":{"day":269.76,"night":268.08,"eve":270.43,"morn":264.98},
      "pressure":978,
      "humidity":47,
      "dew_point":264.4,
      "wind_speed":6.47,
      "wind_deg":17,
      "wind_gust":13.84,
      "weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],
      "clouds":100,"pop":0.93,"snow":3.25,"uvi":1.52
    },
    {
      "dt":1649502000,
      "sunrise":1649477903,
      "sunset":1649528291,
      "moonrise":1649490180,
      "moonset":1649474580,
      "moon_phase":0.25,
      "temp":{"day":279.69,"min":269.31,"max":280.16,"night":275.71,"eve":278.03,"morn":271.25},
      "feels_like":{"day":276.68,"night":272.13,"eve":275.54,"morn":268.85},
      "pressure":987,
      "humidity":33,
      "dew_point":264.45,
      "wind_speed":4.95,
      "wind_deg":309,
      "wind_gust":11.28,
      "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
      "clouds":99,"pop":0.07,"uvi":1.89
    },
    {
      "dt":1649588400,
      "sunrise":1649564124,
      "sunset":1649614838,
      "moonrise":1649581320,
      "moonset":1649562480,
      "moon_phase":0.28,
      "temp":{"day":280.52,"min":272.77,"max":280.52,"night":273.93,"eve":275.92,"morn":274.61},
      "feels_like":{"day":277.89,"night":273.93,"eve":274.78,"morn":272.43},
      "pressure":1007,
      "humidity":29,
      "dew_point":263.31,
      "wind_speed":4.52,
      "wind_deg":315,
      "wind_gust":12.53,
      "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
      "clouds":6,"pop":0,"uvi":2.13
    },
    {
      "dt":1649674800,
      "sunrise":1649650345,
      "sunset":1649701385,
      "moonrise":1649673060,
      "moonset":1649649660,
      "moon_phase":0.32,
      "temp":{"day":280.61,"min":272.4,"max":280.61,"night":274.01,"eve":276.89,"morn":274.49},
      "feels_like":{"day":280.61,"night":272.1,"eve":275.3,"morn":273.14},
      "pressure":1021,
      "humidity":30,
      "dew_point":264,
      "wind_speed":1.78,
      "wind_deg":359,
      "wind_gust":2.4,
      "weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],
      "clouds":4,"pop":0,"uvi":2.51
    },
    {
      "dt":1649761200,
      "sunrise":1649736566,
      "sunset":1649787932,
      "moonrise":1649764920,
      "moonset":1649736480,
      "moon_phase":0.35,
      "temp":{"day":281.89,"min":272.85,"max":282.59,"night":275.98,"eve":278.9,"morn":274.97},
      "feels_like":{"day":281.49,"night":275.98,"eve":278.9,"morn":274.97},
      "pressure":1027,
      "humidity":31,
      "dew_point":265.49,
      "wind_speed":1.39,
      "wind_deg":273,
      "wind_gust":1.67,
      "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
      "clouds":41,"pop":0,"uvi":3
    },
    {
      "dt":1649847600,
      "sunrise":1649822788,
      "sunset":1649874479,
      "moonrise":1649856840,
      "moonset":1649823120,
      "moon_phase":0.38,
      "temp":{"day":281.97,"min":273.81,"max":281.97,"night":276.99,"eve":279.17,"morn":275.6},
      "feels_like":{"day":280.48,"night":276.99,"eve":277.99,"morn":275.6},
      "pressure":1028,
      "humidity":37,
      "dew_point":267.68,
      "wind_speed":2.98,
      "wind_deg":192,
      "wind_gust":3.87,
      "weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],
      "clouds":97,
      "pop":0.2,
      "snow":0.19,
      "uvi":3
    },
    {
      "dt":1649934000,
      "sunrise":1649909011,
      "sunset":1649961026,
      "moonrise":1649948700,
      "moonset":1649909700,
      "moon_phase":0.41,
      "temp":{"day":283.23,"min":276.18,"max":283.84,"night":276.63,"eve":279.32,"morn":276.9},
      "feels_like":{"day":281.36,"night":276.63,"eve":277.59,"morn":275.47},
      "pressure":1025,
      "humidity":41,
      "dew_point":270.19,
      "wind_speed":3.31,
      "wind_deg":199,
      "wind_gust":6.27,
      "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
      "clouds":83,
      "pop":0,
      "uvi":3
    }
  ]
}

for i in vaerdata["daily"]:
    unixtid = i["dt"]
    dato = dt.datetime.fromtimestamp(unixtid)
    temp = i["temp"]["day"] - 273.15
    print(f"Temperatur for {dato} er {temp:.2f} C")
    if "snow" in i:
        print(f"Mengde snø denne dagen var {i["snow"]}mm")
    print("")