from math import exp

def diff_step(energy, density, temp):
    """ Monte Carlo simulation of diffusion for an arbitrary energy function

      Parameters
      ----------
      energy: energy function
                Energy function, takes density array as its argument

      density: array of positive integers
                Number of particles at each position i in the density array

      temp: temperature of diffusion
                Controls how quickly diffusion happens -- affects how often proposed diffusion steps are taken
          
    """

def prob_move(energies, temp):
    """ return probability of accepting move given different energies and temp
    """
    if len(energies)!=2:
        raise TypeError, "Energies must be an array of length 2"

    if temp <= 0:
        raise ValueError, "Temperature must be greater than 0"
    
    if energies[1] <= energies[0]:
        prob = 1
    else:
        prob = exp( -(energies[1] - energies[0]) / temp)

    return prob
