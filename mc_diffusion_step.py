from math import exp
import random

def diff_step(f_energy, density, temp):
    """ Monte Carlo simulation of diffusion for an arbitrary energy function

      Parameters
      ----------
      f_energy: energy function
                Energy function, takes density array as its argument

      density: array of positive integers
                Number of particles at each position i in the density array

      temp: temperature of diffusion
                Controls how quickly diffusion happens -- affects how often proposed diffusion steps are taken
          
    """

    energies[0] = f_energy(density)
    density_new = move_particle(density)

    prob = prob_move(energies, temp)



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

def move_particle(density):
    
    """ choose a particle at random and then move it left or right
        note that moving left is not possible for particles at i=0
        and moving right is not possible for particles at i=end
    """
    i = random.randint(0, len(density)-1)
    if i==0 and density[i] > 0:
        density[0] -= 1
        density[1] += 1
    elif i==len(density)-1 and density[i] > 0:
        density[i]   -= 1
        density[i-1] += 1
    elif i > 0 and density[i] > 0:
        l_or_r = random.choice([-1, 1])
        density[i]          -= 1
        density[i + l_or_r] += 1 
    elif density[i]==0:
        density = move_particle(density)
    else:
        raise ValueError, "density appears to have a negative entry."

    return density
