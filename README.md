# numpy-tests
The benchmarks run_bench.py and run_bench2.py are intended to compare the performance of Intel optimized libraries like numpy and scipy against their stock versions. 
The stock versions of numpy and scipy can be installed using "pip install numpy scipy" command. 
Intel optimized versions of numpy and scipy can be installed from conda channel using "conda install numpy scipy" or by installing Intel oneAPI Analytics toolkit package. 
Benchmark code was taken from https://jwalton.info/Python-MKL-openBLAS/ and http://markus-beuckelmann.de/blog/boosting-numpy-blas.html
To compare the performance benefit of two different versions, create two virtual or conda environments with different numpy/scipy versions installed, and just run below commands:
python run_bench.py
python run_bench2.py
