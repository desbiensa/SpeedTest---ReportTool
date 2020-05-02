import pandas
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from pandas import DataFrame
import csv

x = []
y = []

#IMPORT CSV
with open("C:\Program Files\ookla-speedtest-1.0.0-win64\speed.csv", 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=" ")
#     for row in plots:
#         x.append(str(row[0]))
#         y.append(str(row[0]))

# plt.plot(x,y, marker='o')
# plt.title('Bandwidth Report - To this day')
# plt.xlabel('Mbps')
# plt.ylabel('Date')

# plt.show()
    
    print(plots)
    