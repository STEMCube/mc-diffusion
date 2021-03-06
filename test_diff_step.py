from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from mc_diffusion_step import *

def test_lower_energy():
    """ second energy is lower, so the proposed move should always be accepted
    """
    energies = [2, 1]
    temp = 1
    prob = prob_move(energies, temp)

    assert_equal(prob, 1)

def test_invalid_energies():
    """ try some invalid energies, which should be rejected out of hand
    """ 
    temp = 1

    # array should be length 2
    energies = [1, 2, 3]

    try:
        prob_move(energies, temp)
    except TypeError:
        assert True

    # entries should be real numbers
    energies = ["a", 1]

    try:
        prob_move(energies, temp)
    except TypeError:
        assert True

def test_invalid_temps():
    """ try some invalid temps, which should be rejected out of hand
    """
    energies = [1, 2]

    temp = [1, 2]
    try:
        prob_move(energies, temp)
    except TypeError:
        assert True

    temp = "a"
    try:
        prob_move(energies, temp)
    except TypeError:
        assert True

    temp = -5
    try:
        prob_move(energies, temp)
    except ValueError:
        assert True

    temp = 0
    try:
        prob_move(energies, temp)
    except ValueError:
        assert True

def test_higher_energy():
    """ check probability is in the right range for a higher energy
    """
    temp = 1
    energies = [1, 2]

    prob = prob_move(energies, temp)

    assert_equal( (prob >= 0 and prob <= 1), True )

def test_move_particle():
    """ test particle perturbation is feasible for some known values, and test
        it catches invalid values
    """

    try:
        move_particle([0, 0, 0, 0])
    except ValueError:
        assert True

    try:
        move_particle([1, -1, 0])
    except ValueError:
        assert True

    try: 
        move_particle([2, 5, "a"])
    except TypeError:
        assert True

    # there is only one possible perturbation here
    assert_equal(move_particle([1, 0, 0]), [0, 1, 0])

def test_diff_step():
    """ test overall diffusion step gives feasible output
    """
    temp = 1
    sqr = lambda x : x**2
    energy = lambda x : sum(map(sqr, x))

    density = [1, 0, 0]

    new_density = diff_step(energy, density, temp)

    if new_density==[1, 0, 0] or new_density==[0, 1, 0]:
        assert True
    else:
        raise ValueError, "Output should not be possible."
