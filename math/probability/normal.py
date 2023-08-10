#!/usr/bin/env python3
"""Documentation"""


class Normal:
    """Normal class represents a normal distribution."""
    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the Normal distribution with given data or mean
        and standard deviation.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            self.stddev = float((sum((x - self.mean) ** 2
                                    for x in data) / len(data)) ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score.
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the probability density function (PDF)
        for a given x-value.
    """
        PI = 3.14159265358979323846
        SQRT_TWO_PI = 2.5066282746310002 # sqrt(2 * PI)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        e_to_power = 1
        term = 1
        for i in range(1, 20): # Taylor expansion for e^x
            term *= exponent / i
            e_to_power += term
        return (1 / (self.stddev * SQRT_TWO_PI)) * e_to_power

    def cdf(self, x):
        """Calculates the cumulative distribution function (CDF) for a given x-value.
        """
        Z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        T = 1 / (1 + 0.5 * abs(Z))
        constants = [0.319381530, -0.356563782, 1.781477937, -1.821255978, 1.330274429]
        sum_constants = sum(c * (T ** (i+1)) for i, c in enumerate(constants))
        prob = 1 - (T * sum_constants * ((2 * 3.14159265358979323846) ** -0.5) * (2.718281828459045 ** (-Z * Z / 2)))

        return prob if Z >= 0 else 1 - prob    
    