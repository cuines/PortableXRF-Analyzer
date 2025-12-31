"""Unit tests for quantification methods."""

import sys
sys.path.insert(0, 'src')

from analysis.element_quantification import calculate_concentration

def test_calculate_concentration_fe():
    """Test concentration calculation for Fe (uses integrate_peak)."""
    spectrum = [1, 2, 3, 4, 5]
    result = calculate_concentration(spectrum, 'Fe')
    assert result == 0.15  # sum=15 * 0.01 = 0.15
    print("Fe test passed")

def test_calculate_concentration_pb():
    """Test concentration calculation for Pb (uses deconvolve_peak)."""
    spectrum = [1, 2, 3, 4, 5]
    result = calculate_concentration(spectrum, 'Pb')
    # deconvolve_peak returns 0.123, concentration factor 0.01 => 0.00123
    expected = 0.123 * 0.01
    assert abs(result - expected) < 1e-10
    print("Pb test passed")

def test_calculate_concentration_other():
    """Test concentration calculation for other elements."""
    spectrum = [10, 20, 30]
    result = calculate_concentration(spectrum, 'Cu')
    assert result == 0.6  # sum=60 * 0.01 = 0.6
    print("Other element test passed")

if __name__ == "__main__":
    test_calculate_concentration_fe()
    test_calculate_concentration_pb()
    test_calculate_concentration_other()