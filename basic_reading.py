import pandas as pd
import matplotlib.pyplot as plt
import datetime

date_time_series = []
date_time = datetime.datetime(2018, 1, 2)
date_at_end = datetime.datetime(2018, 1, 3, 23, 59)
step = datetime.timedelta(minutes=1)

while date_time <= date_at_end:
  date_time_series.append(date_time)
  date_time += step

print(date_time_series)

data = pd.read_csv('StormEleanor_2_3_Jan.csv', delimiter=',', header=0)

pressure_data = data['Pair_Avg']

plt.plot(pressure_data)
plt.savefig("pressure.png")



weatherfile = open("StormEleanor_2_3_Jan.csv", "r")

pressure_data = []

for line in weatherfile:
    data_row = line.split(',')
    pressure = data_row[6]
    pressure_data.append(pressure)  #all pressure data will be string type. Not float, as we may wish.

weatherfile.close()

#Try again to skip the first data entry using next()

weatherfile = open("StormEleanor_2_3_Jan.csv", "r")
next(weatherfile)
pressure_data = []
for line in weatherfile:

    data_row = line.split(',')
    pressure = float(data_row[6])
    pressure_data.append(pressure)  #all pressure data will be string type. Not float, as we may wish.

weatherfile.close()