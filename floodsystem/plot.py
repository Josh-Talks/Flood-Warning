import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import *

def plot_water_levels(station, dates, levels):

    # station_name = station
    plt.plot(dates, levels, 'b')
    high_level = station.typical_range[1]
    low_level = station.typical_range[0]
    # plt.plot(t, high_level, 'r')
    # plt.plot(t, low_level, 'b')
    plt.axhline(y=high_level, color='r', linestyle='-', label = "high level")
    plt.axhline(y=low_level, color='g', linestyle='-', label = "low level")

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
