import pandas as pd
#import re
#import pyxlsb
#aqui ver la extensión del archivo y que abra si cambiaron de formato
archivoAduanas = "assets/aduanasDiciembre2020.xls"
#CamposPaTrabajar = ['Tramite': 'tramite','[Doc. Export]':'idExportador','Exportador': 'exportador','[Importe Factura]': 'factura','[Posición Arancelaria]': 'NANDINA','FOB $us': 'fob','Sector': 'sector']
CamposPaTrabajar = ['tramite','idExportador','exportador','factura','NANDINA','fob','sector']
#aqui ver la extensión del archivo y que abra si cambiaron de formato
diccionario = 'diccionario.xlsx'
#eso podemos utilizar para los parametros
#PalabrasClave = 'PalabrasClave.xlsx'
#agarramos el parametro "archivitos" y les hacemos Dataframes y concatenamos
dfArchivo =pd.read_excel(archivoAduanas)#, engine='pyxlsb')
dfArchivoColumnas= dfArchivo.iloc[:,[0,5,6,8,11,14,15]]
dfArchivoColumnas.columns = CamposPaTrabajar    
print("este hay que transformar")
print(dfArchivoColumnas.head)
#dfArchivoColumnas['NANDINAnuevo']=dfArchivoColumnas.NANDINA.map(lambda x:x/10)
print("NANDINA")
print(dfArchivoColumnas['NANDINA']) 
dfArchivoColumnas['NANDINA']=dfArchivoColumnas['NANDINA'].transform(lambda x:x*0.1)
print("NANDINA transformado")
print(dfArchivoColumnas['NANDINA']) 
dfArchivoParaTrabajar = dfArchivoColumnas
print("ArchivoParaTrabajar a ver")
print(dfArchivoParaTrabajar.head)  
print(dfArchivoParaTrabajar.columns)  
###print(dfDatosPaTrabajar.columns)  
#Seleccionamos los campos del diccionario diccionario que nos interesa
dfdiccionarioP = pd.read_excel(diccionario)
print(dfdiccionarioP.head) 
dfdiccionario = pd.DataFrame(dfdiccionarioP, columns=['NANDINA','COD','PRODUCTO'])
print(dfdiccionario.columns)  
valorPorDefecto= "Por identificar"
#Juntamos nuestro Dataframe con Naturalezas tipo BuscarV
resultadoMerge=dfArchivoParaTrabajar.merge(dfdiccionario, on='NANDINA', how='left').fillna(valorPorDefecto)
print("resultado merge")
print(resultadoMerge.head)
print(resultadoMerge.columns)
###dfDatosPaTrabajar['Naturaleza']=resultadoMerge['Naturaleza']
with pd.ExcelWriter('hola.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
    resultadoMerge.to_excel(writer, sheet_name='Resumena') 