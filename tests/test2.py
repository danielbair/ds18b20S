from ds18b20S import DsbS

sensor = DsbS()

TandId = sensor.getIdTemp("F")   # Argument is temperature type C or F or K, default C

print(TandId)   #Print temperatures and ids in dict, key is sensor ID and value is temperature