from ds18b20S import DsbS

sensor = DsbS()

temps = sensor.getTemps("F")   # Argument is temperature type C or F or K, default C

print(temps)   #Print temperatures in list