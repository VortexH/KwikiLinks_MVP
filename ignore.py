#!/usr/bin/python3
""" ignore module """

import geonamescache
import requests

city = requests.get("https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json")

gc = geonamescache.GeonamesCache()

ignore = []

for x in gc.get_countries_by_names():
    ignore.append(x)

for x in gc.get_us_states_by_names():
    ignore.append(x)

for x in city.json():
    ignore.append(x.get("city"))
