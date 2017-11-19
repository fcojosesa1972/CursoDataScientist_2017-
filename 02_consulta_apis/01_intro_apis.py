import requests

url = 'http://www.cartociudad.es/services/api/geocoder/reverseGeocode'
param = {'lng':-3.4244838, 'lat':36.9003409}

r = requests.get(url, param)

print(r.text)
print(r.status_code)
print(r.headers)