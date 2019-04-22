import csv
from matplotlib import pyplot as plt

from datetime import datetime
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')


#get dates high, and low temps from file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    for index, column_header in enumerate(header_row):
        print(index, column_header)

    precipitation, dates = [], []
    #get precipitation and dates for each row
    for row in reader:
        try:
            # we dont want any errors on days without rainfall
            precip = float(row[19])
        except ValueError:
            print('No rainfall for this day')
        else:
            precipitation.append(precip)

        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, precipitation, c='blue')



    plt.title('Daily Precipitation - 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Inches', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
