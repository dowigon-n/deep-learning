# and gate : perceptron

import numpy as np
import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()), 'lib'))
    from common import step
except ImportError:
    print('Library Module Can Not Found')

def AND(x):
    w, b = np.array([0.5, 0.5]), np.array(-0.7)             #학습 결과값

    a = np.sum(x * w) + b
    y = step(a)

    return y
