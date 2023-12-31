#!/usr/bin/env python3
"""Documentation"""


class Exponential():
    """represents exponetial distribution"""
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
            self.lambtha = 1 / float(sum(data) / len(data))

    def pdf(self, x):
        """Calculates the value of the PDF for a given time period"""
        if x < 0:
            return 0
        else:
            e = 2.7182818285  # Euler's number
            return self.lambtha * (e ** (-self.lambtha * x))

    def cdf(self, x):
        """Calculates the cumulative distribution function (CDF)
        for a given time period x.
        """
        if x < 0:
            return 0
        else:
            e = 2.7182818285
            return 1 - (e ** (-self.lambtha * x))
