import pytest

from flaskr import prime


def test_nth_prime():
    expected = -1
    result = prime.get_nth_prime(0)
    assert expected == result

    # (n, expected)
    test_list = [(1, 2), (2, 3), (3, 5), (10, 29), (25, 97)]

    for e in test_list:
        expected = e[1]
        result = prime.get_nth_prime(e[0])
        assert expected == result


def test_nth_prime_wrong_input():
    assert -1 == prime.get_nth_prime(-1)
    with pytest.raises(TypeError):
        prime.get_nth_prime("1")
