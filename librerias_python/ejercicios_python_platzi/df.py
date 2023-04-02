import pandas as pd
import numpy as np

nombre_paises=["China","India","Estados Unidos", "Indonesia","Pakistán","Brasil","Nigeria","Bangladesh","Rusia","México"]
encabezado = ["Poblacion","Porcentaje"]
datos=[[1439,18.47],
            [1380,17.70],  
            [331,4.25],
            [273,3.51],
            [220,2.83],
            [212,2.73],
            [206,2.64],
            [164,2.11],
            [145,1.87],
            [128,1.65]]
paises = pd.DataFrame(datos,index=nombre_paises,columns=encabezado)
print(paises)
print("\n")
print(paises.iloc[0:4])
print("\n")
print(paises.loc["Brasil"])
print("\n")
reglon = pd.Series(name="Japón", data=[126,1.62], index=["Poblacion", "Porcentaje"])
# print(reglon)
print("\n")
paises = paises.append(reglon)
print(paises)
print("\n")
paises.drop(["Japón"],axis=0,inplace=True)
print(paises)
print("\n")
print(paises.cumsum())









# df = pd.DataFrame({"columna1":[1,2,3],
#                                 "Columna2":[4,5,6],
#                                 "Columna3":[7,8,9,]})
# print(df)
# print(df.shape)
# nombres = ["columna0", "columna1","columna2"]
# df.columns=nombres
# print(df)








# pd.set_option("display.max_columns", 20)
# df = pd.read_csv("StudentsPerformance.csv")
# print(df)
# print(df.sum(axis=1))