from datetime import datetime
import pytz

seoul_timezone = pytz.timezone("Asia/Seoul")
seoul_date = datetime.now(seoul_timezone)
seoul_city =  seoul_date.strftime("%d, %m, %Y, %H, %M, %S")
print("Seúl, Corea del Sur: " + seoul_city)

# print("Seúl, Corea del Sur: " + seoul_date.strftime("%d, %m, %Y, %H, %M, %S"))


berlin_timezone = pytz.timezone("Europe/Berlin")
berlin_datetime = datetime.now(berlin_timezone)
berlin_city = berlin_datetime.strftime("%d, %m, %Y, %H, %M, %S")
print("Berlín, Aelmania: " + berlin_city)

moscow_timezone = pytz.timezone("Europe/Moscow")
moscow_datetime = datetime.now(moscow_timezone)
moscow_city = moscow_datetime.strftime("%d, %m, %Y, %H, %M, %S")
print("Moscú, Rusia: " + moscow_city)

