import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pympler

from pympler import asizeof
from pylops.signalprocessing import FFT


def DFT(x):
    """Function to calculate the discrete Fourier Transform of a 1D real-valued signal x
    
    Adapted from https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter24.02-Discrete-Fourier-Transform.html
    
    """
    N = len(x)
    n = np.arange(N)
    k = np.arange(N//2 + 1).reshape((N//2 + 1, 1))
    D = np.exp(-2j * np.pi * k * n / N)
    
    X = np.dot(D, x)
    
    return X, D


def FFT_memory():
    """Memory footprint of FFT operator
    """
    nn = (10 ** np.arange(2, 4, 0.5)).astype(np.int32)

    mem_DFT = []
    mem_FFT = []
    mem_Fop = []
    for n in nn:
        x = np.arange(n)
        _, D = DFT(x)
        Fop = FFT(n, engine='scipy', real=True)
        mem_DFT.append(asizeof.asizeof(D))
        mem_FFT.append(asizeof.asizeof(n))
        mem_Fop.append(asizeof.asizeof(Fop))

    plt.figure(figsize=(6, 4))
    plt.semilogy(nn, mem_DFT, '.-k', label='DFT')
    plt.semilogy(nn, mem_FFT, '.-r', label='FFT')
    plt.semilogy(nn, mem_Fop, '.-g', label='FFTop')
    plt.legend()
    plt.title('Memory comparison')
    plt.xlabel('Vector size')