#!/usr/bin/python3
import cab_app
cab_app.cab_count()

while (1):
    print("Cab queue")
    print(cab_app.cab_list)
    if cab_app.run_station() == 0:
       exit()
