from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from mc_diffusion_step import diff_step, prob_move

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

#def test_invalid_temps():

#def test_higher_energy():
