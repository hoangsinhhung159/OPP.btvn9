minutes = 42
seconds = 42
totalseconds = minutes*60+seconds
print(totalseconds)
km = 10
mile = 1.61
totalmiles = km/mile
print(totalmiles)
pace_seconds = totalseconds/totalmiles
totalminutes = minutes+42/60
pace_minutes = totalminutes/totalmiles
average_pace = f"{pace_minutes} minutes {pace_seconds} seconds"
print(average_pace)
totalhours = totalseconds/3600
average_speed = totalmiles/totalhours
print(average_speed)