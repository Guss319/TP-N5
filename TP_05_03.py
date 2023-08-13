import datetime
fecha=datetime.datetime.now().date().strftime("%y-%m-%d")
hora=datetime.datetime.now().time().strftime("%H:%M")

print(f"hoy es {fecha} y son las {hora}")