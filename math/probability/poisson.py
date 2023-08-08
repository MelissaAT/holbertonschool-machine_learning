#!/usr/bin/env python3
"""Documentation"""


class Poisson:
    """Poisson class represents a Poisson distribution."""
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculates the probability mass function (PMF)
        for a given number of "successes" k."""
        k = int(k)
        if k < 0:
            return 0
        else:
            e = 2.7182818285  # Euler's number
            factorial_k = 1
            for i in range(1, k + 1):
                factorial_k *= i
            return (e ** -self.lambtha) * (self.lambtha ** k) / factorial_k

    def cdf(self, k):
        """Calculates the cumulative distribution function
        (CDF) for a given number of "successes" k."""
        k = int(k)
        if k < 0:
            return 0
        else:
            cdf_value = 0
            for i in range(k + 1):
                cdf_value += self.pmf(i)
            return cdf_value
