#!/usr/bin/env python3
"""Documentation"""


class Poisson:
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
        pmf_value = 1
        for i in range(1, k + 1):
            pmf_value *= self.lambtha / i
        pmf_value *= (2.71828 ** (-self.lambtha))
        return pmf_value

    def cdf(self, k):
        k = int(k)
        if k < 0:
            return 0
        cdf_value = 0
        probability = 1
        for i in range(k + 1):
            cdf_value += probability * (2.71828 ** (-self.lambtha))
            probability *= self.lambtha / (i + 1)
        return cdf_value

    def __str__(self):
        return f"Poisson distribution with lambda = {self.lambtha}"
