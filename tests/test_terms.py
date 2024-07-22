import numpy as np
import pandas as pd

from atomic_term_symbol_calculator.terms import calc_microstates

def test_calc_microstates():
    assert calc_microstates(2, 1) == 2  # 1 electron in s shell
    assert calc_microstates(6, 2) == 15 # 2 electrons in p shell