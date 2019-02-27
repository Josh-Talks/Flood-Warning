import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    dates = matplotlib.dates.date2num(dates)
    if len(dates) > 1:
        x = np.linspace(max(dates), min(dates), len(dates))
        d0 = x[0]
        p_coeff = np.polyfit(x-d0, levels, p)
        poly = np.poly1d(p_coeff)
        return poly, x
    else:
        return None

def current_gradient(poly):
    grad = np.polyder(poly)
    