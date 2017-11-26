import requests
import json

url = 'http://nominatim.openstreetmap.org/reverse'
param = {'format':'json', 'lat':51.4965946,'lon': -0.1436476}
r_Nom = requests.get(url, param)

salida = json.loads(r_Nom.text)
print(salida)

url_crimes = 'https://data.police.uk/api/crimes-street/all-crime'
param = {'format':'json', 'lng':-0.1436476, 'lat':51.4965946, 'date':'2017-04'}
r_Crimes = requests.get(url_crimes, param)

salida = json.loads(r_Crimes.text)
np_salida = np.array(salida)

contador = {}
for elemento in salida :
    if elemento['category'] in contador :
        contador[elemento['category']] += 1
    else :
        contador[elemento['category']] = 1
        
print(contador)    
