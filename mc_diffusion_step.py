from math import exp
import random

def diff_step(f_energy, density, temp=1):
    """ Monte Carlo simulation of diffusion for an arbitrary energy function

      Parameters
      ----------
      f_energy: energy function
                Energy function, takes density array as its argument

      density: array of positive integers
                Number of particles at each position i in the density array

      temp: temperature of diffusion
                Controls how quickly diffusion happens -- affects how often proposed diffusion steps are taken
                Default value is 1
          
    """

    energies = []

    energies.append(f_energy(density))

    density_prop = move_particle(density)
    energies.append(f_energy(density_prop))

    prob_m = prob_move(energies, temp)

    # comparison probability... whether to move is a random variable, scaled against this
    prob_c = random.random()

    if prob_m >= prob_c:
        density = density_prop
    else:
        pass

    return density

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

    # check density is made from positive integers
    for n in density:
        if n < 0:
            raise ValueError, "All elements of density vector must be positive."
        elif not isinstance(n, int):
            raise TypeError, "All elements of density vector should be integers."

    # check density is not zeros vector... need to catch this to prevent infinite recursion 
    if all(n==0 for n in density):
        raise ValueError, "All elements of density vector are zero."

    density_prop = list(density)

    if i==0 and density_prop[i] > 0:
        density_prop[0] -= 1
        density_prop[1] += 1
    elif i==len(density_prop)-1 and density_prop[i] > 0:
        density_prop[i]   -= 1
        density_prop[i-1] += 1
    elif i > 0 and density_prop[i] > 0:
        l_or_r = random.choice([-1, 1])
        density_prop[i]          -= 1
        density_prop[i + l_or_r] += 1 
    elif density_prop[i]==0:
        density_prop = move_particle(density_prop)
    else:
        raise ValueError, "density_prop has somehow taken an invalid value after initial checks. This should never happen."

    return density_prop
