#!/usr/bin/python
from mc_diffusion_step import *
from default_energy import *
from matplotlib import pyplot as plt
from time import sleep

""" examples of using the Monte Carlo diffusion simulator """ 
density = [500, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1]

plt.plot(density)
plt.show(block=False)
# using the default energy function
for i in range(1, 100000):
    density = diff_step(default_energy, density, 100)
    if i % 1000 == 0:
        plt.plot(density)
        sleep(0.05)
        plt.draw()
        plt.clf()

print density
plt.show(block=True)
plt.plot(density)
plt.draw()

# using a lambda energy function
