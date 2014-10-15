from nose.tools import assert_true, assert_equal, assert_not_equal, assert_raises
from diffusion_model import energy

def test_energy_known():
    """ test with known result 
        TODO: use proper floating point comparison
    """
    argument = [2]
    calc_result = energy(argument)
    true_result = 1
    assert_equal(calc_result, true_result)

def test_negative_density():
    """ test with a negative element in density vector """
    argument = [1, 1, -1]
    try:
        energy(argument)
    except ValueError:
        assert True 
