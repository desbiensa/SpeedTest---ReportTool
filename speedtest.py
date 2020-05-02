from subprocess import run
import subprocess
from datetime import datetime
import json
import pandas as pd
from pandas import DataFrame

myOut = subprocess.Popen(["C:\Program Files\ookla-speedtest-1.0.0-win64\speedtest.exe", "-f", "json", "-s", "911"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

stdout, stderr = myOut.communicate()

theJSON = json.loads(stdout)
a = datetime.now()
b = theJSON["download"]["bandwidth"]/125000
c = theJSON["upload"]["bandwidth"]/125000

#TRIM DATA
time = a.strftime("%H:%M")
date = a.today().strftime('%Y%m%d')
down = "%.2f" % b
up = "%.2f" % c


#SET DATA and HEADERS
d = {'Time': [time], "Date": [date], "Download": [down], "Upload": [up]}
df = pd.DataFrame(data=d)
#print(df)

#WRITE to CSV
df.to_csv('C:\Program Files\ookla-speedtest-1.0.0-win64\speed.csv', mode="a", sep='\t', index=False, header=False)