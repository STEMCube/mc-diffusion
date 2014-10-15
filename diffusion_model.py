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
        total = total + coeff/2 * n * (n-1)

    return total
