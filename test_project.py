from project import Particle,calc_dist,calc_dir,kinetic_energy,potential_energy
import pytest

"""
UNIT TESTS
"""

def test_calc_dist():
    p1 = Particle(200,300,1,0,10)
    p2 = Particle(100,400,0,-1,15)
    assert calc_dist(p1, p2) == (-100,100,141.4213562373095)

def test_calc_dir():
    assert calc_dir(-100,100,141.4213562373095) == (-0.7071067811865475, 0.7071067811865475)

def test_kinetic_energy():
    p = Particle(200,300,1,0,10)
    assert kinetic_energy(p) == 5

def test_potential_energy():
    particles = [Particle(200,300,1,0,10), Particle(100,400,0,-1,15)]
    assert potential_energy(particles) == pytest.approx(-106.0660171779821)