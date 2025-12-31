"""Functions for calculating element concentrations."""

from . import algorithms

def calculate_concentration(spectrum, element):
    """Calculate concentration of an element from spectrum.
    
    Args:
        spectrum: list or array of intensities
        element: string element symbol
        
    Returns:
        float concentration
    """
    # Simple peak integration for all elements
    peak_area = algorithms.integrate_peak(spectrum, element)
    # Placeholder conversion factor
    concentration = peak_area * 0.01
    return concentration
