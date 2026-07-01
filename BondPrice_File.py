import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    periods = np.arange(1, n + 1)

    cashflows = np.full(n, coupon, dtype=float)
    cashflows[-1] += face

    price = np.sum(cashflows / (1 + r) ** periods)

    return price
