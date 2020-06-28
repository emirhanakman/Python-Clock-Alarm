import time

""" localtime """

hour = eval(input("Saat Giriniz : "))
minute = eval(input("Dakika Giriniz : "))

while True:
	saat = time.localtime(time.time())
	if hour == saat.tm_hour and minute == saat.tm_min:
		print("\nAlarm Çaldı!\nSaat ",saat.tm_hour, ":",saat.tm_min)
		break
	else:
		pass

print("\nProgram Kapatılıyor....")