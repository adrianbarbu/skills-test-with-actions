# System Modules
import sys
import os

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
     """Test with n=10."""
     # Arrange
     n = 10

     # Act
     result = get_nth_fibonacci(n)

     # Assert
     assert result == 55


# -----------------------------
# Tests for area_of_circle
# -----------------------------
def test_area_of_circle_zero():
    assert area_of_circle(0) == 0

def test_area_of_circle_positive():
    radius = 2
    expected = math.pi * radius**2
    assert area_of_circle(radius) == expected

def test_area_of_circle_large_value():
    radius = 1_000
    expected = math.pi * radius**2
    assert area_of_circle(radius) == expected

def test_area_of_circle_negative_raises():
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(-5)

# -----------------------------
# Tests for get_nth_fibonacci
# -----------------------------
def test_fibonacci_zero():
    assert get_nth_fibonacci(0) == 0

def test_fibonacci_one():
    assert get_nth_fibonacci(1) == 1

def test_fibonacci_small_numbers():
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(5) == 5
    assert get_nth_fibonacci(10) == 55

def test_fibonacci_negative_raises():
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(-1)

def test_fibonacci_large_number():
    # Just check it runs and gives the right result for a known value
    assert get_nth_fibonacci(20) == 6765
