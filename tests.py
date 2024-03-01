import pytest

from points import read_points, Point


def isnamedtupleinstance(x):
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple:
        return False
    f = getattr(t, "_fields", None)
    if not isinstance(f, tuple):
        return False
    return all(type(n) == str for n in f)


def test_point():
    point = Point(20, 10)

    assert isnamedtupleinstance(point)
    assert point.x == 20
    assert point.y == 10


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("10,20;20,10", [Point(10.0, 20.0), Point(20.0, 10.0)]),
        ("1.234,0;10,20", [Point(1.234, 0.0), Point(10.0, 20.0)]),
    ],
)
def test_read_points(test_input, expected):
    assert read_points(text=test_input) == expected


@pytest.mark.parametrize(
    "test_input,separator,expected",
    [
        ("10,20_20,10", "_", [Point(10.0, 20.0), Point(20.0, 10.0)]),
        (
            "1.234,0*10,20*1.234,0*-10,20",
            "*",
            [
                Point(1.234, 0.0),
                Point(10.0, 20.0),
                Point(1.234, 0.0),
                Point(-10.0, 20.0),
            ],
        ),
    ],
)
def test_read_points_custom_separator(test_input, separator, expected):
    assert read_points(text=test_input, separator=separator) == expected


def test_docstrings():
    assert read_points.__doc__ is not None
