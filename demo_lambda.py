#!/usr/bin/python
from mc_diffusion_step import *
from matplotlib import pyplot as plt
from time import sleep

""" example of using the Monte Carlo diffusion simulator """ 

cube = lambda x : x**3
func_energy = lambda x : sum(map(cube, x))

density = [500, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1]

plt.plot(density)
plt.show(block=False)
# using the default energy function
for i in range(1, 100000):
    density = diff_step(func_energy, density, 100)
    if i % 1000 == 0:
        plt.plot(density)
        sleep(0.05)
        plt.draw()
        plt.clf()

print density
plt.show(block=True)
plt.plot(density)
plt.draw()
