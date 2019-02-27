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
        poly_deriv = poly.deriv(m=1)
        print(poly_deriv)
        return poly, x, poly_deriv
    else:
        return None

def current_gradient(poly, dates, levels, p):
    poly, x, poly_deriv = polyfit(dates, levels, p)
    x1 = np.linspace(x[0], x[-1], 30)
    current_grad = poly_deriv(x1[-1] - x[0])
    print("current gradient")
    print(current_grad)

    return current_grad
