import pandas as pd
#import re
#import pyxlsb
#aqui ver la extensión del archivo y que abra si cambiaron de formato
archivoAduanas = "assets/aduanasDiciembre2020.xls"
#con estos campos vamos a trabajar
CamposPaTrabajar = ['tramite','idExportador','exportador','factura','NANDINA','fob','sector']
#tal vez volverlo matriz json para no tener que manejar muchos exceles
diccionario = 'diccionario.xlsx'

#cargamos el archivo de aduanas
dfArchivo =pd.read_excel(archivoAduanas)#, engine='pyxlsb')
#seleccionamos solo las columnas relevantes
dfArchivoColumnas= dfArchivo.iloc[:,[0,5,6,8,11,14,15]]
#generamos un dataframe con los nombres mas cortos oe
dfArchivoColumnas.columns = CamposPaTrabajar    

#transformamos la columna para que sea comparable con el diccionario
dfArchivoColumnas['NANDINA']=dfArchivoColumnas['NANDINA'].transform(lambda x:x*0.1)

dfArchivoParaTrabajar = dfArchivoColumnas

#Seleccionamos los campos del diccionario diccionario que nos interesa
dfdiccionarioP = pd.read_excel(diccionario)
print(dfdiccionarioP.head) 
dfdiccionario = pd.DataFrame(dfdiccionarioP, columns=['NANDINA','COD','PRODUCTO'])
print(dfdiccionario.columns)  
valorPorDefecto= "No es minerales"
#Juntamos nuestro Dataframe con el diccionario tipo BuscarV
resultadoMerge=dfArchivoParaTrabajar.merge(dfdiccionario, on='NANDINA', how='left').fillna(valorPorDefecto)
print("resultado merge")
#exportamos a excel

with pd.ExcelWriter('hola.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
    resultadoMerge.to_excel(writer, sheet_name='Resumena') 