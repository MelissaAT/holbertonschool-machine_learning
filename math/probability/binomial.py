class Binomial:
    """Binomial class represents a binomial distribution."""
    
    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the Binomial distribution with given data,
        number of trials, or probability of success.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n) # Saving n as an integer
            self.p = float(p) # Saving p as a float
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            
            # Calculating p first
            p = sum(data) / (len(data) * max(data))
            # Calculating n and rounding to the nearest integer
            n = round(sum(data) / p)
            # Recalculating p
            p = sum(data) / (len(data) * n)
            
            self.n = n
            self.p = p
