import numpy as np

from pynufft import NUFFT
from pylops import LinearOperator


class NonUniformFFT(LinearOperator):
    """Non-uniform FFT operator.

    Performs non-uniform FTT and IFFT using ``pynufft``

    Parameters
    ----------
    nt : :obj:`int`
        Number of time samples
    f : :obj:`numpy.ndarray`
        List of frequency along which the non-uniform FTT is computed (must be 
        normalized between -pi to pi)
    dtype : :obj:`str`, optional
        Type of elements in input array.
    name : :obj:`str`, optional
        Name of operator (to be used by :func:`pylops.utils.describe.describe`)

    """
    def __init__(self, nt, f, dtype="complex128", name="F"):
        self.nt = nt
        self.nufftobj = NUFFT()
        self.nufftobj.plan(f, (nt,), (2 * nt,), (6 , ))
        super().__init__(dtype=np.dtype(dtype), dims=(nt, ), dimsd=(f.size, ), name=name)

    def _matvec(self, x):
        y = self.nufftobj.forward(x) / np.sqrt(np.prod(self.nufftobj.Kd))
        return y
    
    def _rmatvec(self, x):
        y = self.nufftobj.adjoint(x) * np.sqrt(np.prod(self.nufftobj.Kd))
        return y