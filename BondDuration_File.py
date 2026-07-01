import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    periods = np.arange(1, n + 1)
    times = periods / ppy

    cashflows = np.full(n, coupon, dtype=float)
    cashflows[-1] += face

    present_values = cashflows / (1 + r) ** periods
    price = np.sum(present_values)

    duration = np.sum(times * present_values) / price

    return duration
