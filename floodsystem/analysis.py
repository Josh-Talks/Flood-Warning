import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from datafetcher import *

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x - x[0], y , 4)
    poly = np.poly1d(p_coeff)
    plt.plot(x, y, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))
    plt.show()