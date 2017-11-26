import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as BeSo
import lxml
import html

def lastMonthDay (year, month) :
    '''La función devuelve el último día del mes del año pasado por parámetros.
    El año y el mes han de tener un formato numérico.'''
    import calendar
    month_list = calendar.monthcalendar(year, month)
    lastWeek = month_list[len(month_list)-1]
    while lastWeek[len(lastWeek)-1] == 0 :
        lastWeek.remove(0)
    return lastWeek[len(lastWeek)-1]


def extractData (year, MetStation ):
    ''' Función para la recuperación de la información de la página de meteorología.
        Recupera la información por día y hora para el año indicado de temperatura, 
        dirección y velocidad del viento.
    Parametro de entrada : AÑO, Estacion Meteorológica
    Parametro de salida  : Data Frame con la información.'''
    fecha_indice = []
    fecha_fin = []
    hora_fin =[]
    temp_fin = []
    windDir_fin = []
    windSpeed_fin = []
    #Preparamos un bucle para los meses del año.
    for x in range(1,13) :
        print('Mes ' + str(x))
        # Preparación de los parametros para la consulta a la página.
        num_days = lastMonthDay(year,x)
        param = {'ord':'REV', 'decoded':'yes', 'ndays':num_days, 'ano':year, 'mes':x, 'day':num_days, 'hora':24, 'ind':MetStation}
        res = requests.get('http://www.ogimet.com/cgi-bin/gsynres', param)
        sheet = BeSo(res.content, 'html.parser')
        table = sheet.find_all('table')[2]
        df = pd.read_html(str(table))[0].iloc[:,0:9]
        
        #Incializamos las variables para la incorporacion 
        fecha = np.array(df.loc[:,'Fecha'][2:])
        hora = np.array(df.loc[:]['T(C)'][2:])
        temp = np.array(df.loc[:]['Td(C)'][2:])
        windDir = np.array(df.loc[:]['ffkmh'][2:])
        windSpeed = np.array(df.loc[:]['P0hPa'][2:])
        for i in range(len(fecha)-1) :
            fecha_indice.append(fecha[i] + ' ' + hora[i])
            fecha_fin.append(fecha[i])
            hora_fin.append(hora[i])
            temp_fin.append(temp[i])
            windDir_fin.append(windDir[i])
            windSpeed_fin.append(windSpeed[i])
        # Tratamos el HTML recibido para incorporarlo en el DataFrame
    # Devolvemos la información en el DataFrame
    
    data = {'fecha':pd.Series(fecha_fin, index=fecha_indice), 
            'hora':pd.Series(hora_fin, index=fecha_indice), 
            'temp':pd.Series(temp_fin, index=fecha_indice), 
            'WD':pd.Series(windDir_fin, index=fecha_indice), 
            'WS':pd.Series(windSpeed_fin, index=fecha_indice)}
    return pd.DataFrame(data)


Salida = extractData(2008,'08221')

Salida