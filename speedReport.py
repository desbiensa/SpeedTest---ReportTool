import pandas as pd
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#IMPORT CSV + PARSE Data & Time
df = pd.read_csv('C:\Program Files\ookla-speedtest-1.0.0-win64\speed.csv', parse_dates=[['Date', 'Time']])

def main():

    #TRIM last 24hours
    now = datetime.now().replace(microsecond=0)
    then = timedelta(days=1)
    ab = df[df.Date_Time >= (now - then)]

    #PLOT "To this Day"
    df.plot(x = 'Date_Time', y = ['Download', 'Upload'], figsize=(15 ,8), grid = True)

    #PLOT "Last 24hours"
    #ab.plot(x = 'Date_Time', y = ['Download', 'Upload'], figsize=(15 ,8), grid = True)

    #LABELS
    plt.xlabel('Date & Time')
    plt.ylabel('Mb/per Sec.')
    plt.title('Videotron - Download & Upload Bandwidth')

    #OUTPUT
    #plt.show()

    fig = go.Figure()

    fig.add_trace(go.Scatter(x = df.Date_Time, y = df.Download, name = 'Download', line=dict(color = 'royalblue'))),
    fig.add_trace(go.Scatter(x = df.Date_Time, y = df.Upload, name = 'Upload', line=dict(color = 'orange')))

    #fig = px.line(ab, x = 'Date_Time', y = 'Download', title= 'test')

    fig.update_layout(title='Videotron - Download & Upload Bandwidth',
                    xaxis_title='Date & Time',
                    yaxis_title='Mb/per Sec.')

    fig.show()

    #fig.write_html("report.html")

if __name__ == "__main__":
    main()