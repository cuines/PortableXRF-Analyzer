"""Unit tests for quantification methods."""

import sys
sys.path.insert(0, 'src')

from analysis.element_quantification import calculate_concentration

def test_calculate_concentration():
    """Test concentration calculation."""
    spectrum = [1, 2, 3, 4, 5]
    result = calculate_concentration(spectrum, 'Fe')
    assert result == 0.15  # sum=15 * 0.01 = 0.15
    print("Test passed")

if __name__ == "__main__":
    test_calculate_concentration()
