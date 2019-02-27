import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import *
import numpy as np
from floodsystem.analysis import *


def plot_water_levels(station, dates, levels):
    station_name = station
    plt.plot(dates, levels, 'b')
    high_level = station.typical_range[1]
    low_level = station.typical_range[0]
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


def plot_water_level_with_fit(station, dates, levels, p):
    poly, x, poly_deriv = polyfit(dates, levels, p)
    plt.plot(dates, levels, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))
    plt.plot(x1, np.linspace(station.typical_range[0], station.typical_range[0], len(x1)))
    plt.plot(x1, np.linspace(station.typical_range[1], station.typical_range[1], len(x1)))
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout
    plt.legend()
    plt.show()

