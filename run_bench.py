#! /usr/bin/env python3

import os.path as path
import numpy as np
import scipy.stats
import pandas as pd
import timeit
import sys


def np_fft_fft():
    x = np.random.rand(1000000)
    time = timeit.timeit(lambda: np.fft.fft(x), number=100)
    return time


def np_fft_fft2():
    x = np.random.rand(1000, 1000)
    time = timeit.timeit(lambda: np.fft.fft2(x), number=100)
    return time


def np_fft_fftn():
    x = np.random.rand(101, 103, 105)
    time = timeit.timeit(lambda: np.fft.fftn(x), number=100)
    return time


def np_linalg_inv():
    x = np.random.rand(100, 100)
    while np.linalg.det(x) == 0:
        x = np.random.rand(1000, 1000)
    time = timeit.timeit(lambda: np.linalg.inv(x), number=100)
    return time


def np_linalg_cholesky():
    x = np.random.rand(1000, 1000)
    # Create positive semi-definite matrix
    y = np.dot(x, x.T)
    time = timeit.timeit(lambda: np.linalg.cholesky(y), number=100)
    return time


def np_linalg_det():
    x = np.random.rand(100, 100)
    time = timeit.timeit(lambda: np.linalg.det(x), number=100)
    return time


def np_random_uniform():
    time = timeit.timeit(lambda: np.random.uniform(-1, 1, 1000000), number=1000)
    return time


def scipy_stats_uniform_rvs():
    time = timeit.timeit(lambda: scipy.stats.uniform.rvs(-1, 1, 1000000), number=1000)
    return time


def np_random_normal():
    time = timeit.timeit(lambda: np.random.normal(size=200000), number=1000)
    return time


def scipy_stats_norm_rvs():
    time = timeit.timeit(lambda: scipy.stats.norm.rvs(size=200000), number=1000)
    return time


def np_random_gamma():
    time = timeit.timeit(lambda: np.random.gamma(5.2, 1, 100000), number=1000)
    return time


def scipy_stats_gamma_rvs():
    time = timeit.timeit(lambda: scipy.stats.gamma.rvs(5.2, 1, size=100000),
            number=1000)
    return time


def np_random_poisson():
    time = timeit.timeit(lambda: np.random.poisson(7.6, 50000), number=1000)
    return time


def scipy_stats_poisson_rvs():
    time = timeit.timeit(lambda: scipy.stats.poisson.rvs(7.6, size=50000),
            number=1000)
    return time


def run_tests():
    #tests = []
    #times = []
    for test in [
            np_linalg_inv,
            np_linalg_cholesky,
            np_linalg_det,
            np_random_uniform,
            np_random_normal,
            np_random_gamma,
            np_random_poisson,
            scipy_stats_uniform_rvs,
            scipy_stats_norm_rvs,
            scipy_stats_gamma_rvs,
            scipy_stats_poisson_rvs,
            np_fft_fft,
            np_fft_fft2,
            np_fft_fftn]:

        #times.append(test())
        #tests.append(test.__name__)
        print("Time for ", test.__name__, test()) 
    #df = pd.DataFrame({"test": tests, "time": times})
    #df.to_csv(path.join('output', "{}.csv".format(install)), index=False)

if __name__ == "__main__":
    #install = sys.argv[1]
    run_tests()

