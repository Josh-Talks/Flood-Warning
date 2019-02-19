import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import *

def plot_water_levels(station, dates, levels, high_level, low_level):
    t = dates
    level = levels

    station_name = station
    plt.plot(t, level, 'g')
    plt.plot(t, high_level, 'r')
    plt.plot(t, low_level, 'b')

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
