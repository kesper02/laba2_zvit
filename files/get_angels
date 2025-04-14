# test_figure.py
from figure import Figure

def test_get_angles_triangle():
    fig = Figure("трикутник", 5)
    assert fig.get_angles == 3

def test_get_angles_square():
    fig = Figure("квадрат", 5)
    assert fig.get_angles == 4

def test_invalid_figure_type():
    import pytest
    with pytest.raises(AssertionError):
        Figure("коло", 5)
