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
            self.stddev = float((sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5)

    def z_score(self, x):
        """Calculates the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score.
        """
        return self.mean + z * self.stddev