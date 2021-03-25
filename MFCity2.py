#Use OpenWeather's OneCall api, excluding 'minutely', 'hourly' and 'alerts'

import requests
import json
import time
from datetime import date
from datetime import timedelta
import datetime 

today = datetime.datetime.now()

def main():
	while True:
		global FileCity2
		FileCity2=open('FileCity2.txt','w')
		AskCity1()
		global today
		today = datetime.datetime.now()
		FileCity2.write(f"\nLast uodate: {today}")
		FileCity2.write("\nData: FileCity2")
		FileCity2.close()
		
		time.sleep(21600) #6 hours interval between each update
		#time.sleep(3) #For testing, use this command

def AskCity1():
	t=requests.get(" ").json() #use your openweather api link here, with lat. and lon. of the city
	listdaily=t["daily"]
	day=0
	for i in listdaily:
		wclouds=i["clouds"]		
		datet=date.today()+timedelta(days=day)
		datet=int(datet.strftime("%d"))
		if "rain" in i:
			mm=i["rain"]
			FileCity2.write(f"Clouds in day {datet}: {wclouds}%, {mm}mm rain\n")
		else:
			FileCity2.write(f"Clouds in day {datet}: {wclouds}%\n")
		global today	
		day+=1
main()

