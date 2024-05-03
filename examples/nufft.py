import numpy as np

from pynufft import NUFFT
from pylops import LinearOperator


class NonUniformFFT(LinearOperator):
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