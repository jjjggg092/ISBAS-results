
import sys, subprocess, os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta

if len(sys.argv) != 4:
    print('''Missing Arguments, Usage:\n
    python plot_ts.py (disp_file.txt) (latitude) (longitude)\n''')
    sys.exit()

lat = float(sys.argv[2])
lon = float(sys.argv[3])
files = sys.argv[1]
min_lat = lat - 0.0001
max_lat = lat + 0.0001
min_lon = 360 + (lon - 0.0001)
max_lon = 360 + (lon + 0.0001)
print(files)

a = subprocess.check_output(['gmt','grd2xyz','rate_mm_yr.grd','-R' + str(min_lon) + '/' + str(max_lon) + '/' + str(min_lat) + '/' + str(max_lat), '-C' ])


a = a.decode("utf-8").split('\n')
index = -1
print(len(a)-2)
for i in range(len(a)-1):
    if 'NaN' not in a[i]:
        index = i
        break

if index == -1:
    print('No data found, try with another location!')
    sys.exit()
mean_los = round(float(a[index].split('\t')[-1]),2)
rate = []
dates = []
with open(files) as f:
    lines = f.readlines()
    for line in lines:
        b = subprocess.check_output(['gmt','grd2xyz',line,'-R' + str(min_lon) + '/' + str(max_lon) + '/' + str(min_lat) + '/' + str(max_lat), '-C' ])
        b = b.decode('utf-8').split('\n')
        rate.append(float(b[index].split('\t')[-1]))
        #print(float(b[0].split('\t')[-1]))

with open('baseline_table.dat') as f:
    lines = f.readlines()
    for line in lines:
        dates.append(line[15:19] + '-' + line[19:21] + '-' + line[21:23])
dates = sorted(dates, key=lambda d: tuple(map(int, d.split('-'))))
for i in range(len(dates)):
    dates[i] = datetime.strptime(dates[i], '%Y-%m-%d')
    print(dates[i],rate[i])
plt.style.use('seaborn-dark-palette')
plt.figure(figsize=(10, 5))
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.gca().xaxis.set_major_locator(mpl_dates.MonthLocator(interval=4))
plt.plot_date(dates, rate, linestyle = 'solid', marker=",", color='black' )
plt.plot_date(dates, rate, linestyle = 'none', marker="^", color='red' )
plt.gcf().autofmt_xdate()
plt.xlabel('Time')
plt.ylabel('Deformation (mm/year)')
plt.title(f'Line Of Sight (2015-2020)\nMean LOS: {mean_los}mm/yr\nLon: {lon}, Lat: {lat}')
plt.show()
