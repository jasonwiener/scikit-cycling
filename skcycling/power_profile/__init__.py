"""
The :mod:`skcycling.power_profile` module include management function for
record power profile.
"""

from .rpp import Rpp
from .rpp import compute_ride_rpp
from .rpp import _rpp_parallel

__all__ = ['Rpp',
           'compute_ride_rpp',
           '_rpp_parallel']