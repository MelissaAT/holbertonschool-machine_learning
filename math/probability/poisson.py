#!/usr/bin/env python3
"""Documentation"""


class Poisson():
    """represents poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        k = int(k)
        if k < 0:
            return 0
        import math
        pmf = (math.exp(-self.lambtha) * self.lambtha ** k) / math.factorial(k)
        return pmf

    def cdf(self, k):
        k = int(k)
        if k < 0:
            return 0
        import math
        cdf = 0
        for i in range(k + 1):
            cdf += (math.exp(-self.lambtha) * self.lambtha ** i / math.factorial(i))
        return cdf
        