def energy(density, coeff=1.0):
    """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
    """

    total = 0

    for n in density:
        if n < 0:
            raise ValueError, "All elements of density vector must be negative."
        elif not isinstance(n, int):
            raise TypeError, "All elements of density vector should be integers."
        total = total + n * (n-1)

    total = coeff/2 * total

    return total
