#!/bin/bash
# 
# Installer for lunateaching environment
# 
# Run: ./install_env.sh
# 
# M. Ravasi, 27/04/2024

echo 'Creating lunateaching environment'

# create conda env
conda env create -f environment.yml
source  $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate lunateaching
conda env list
echo 'Created and activated environment:' $(which python)

# check pylops and pyproximal work as expected
echo 'Checking pylops and pyproximal versions and running a command...'
python -c 'import numpy as np; import pylops; print(pylops.__version__); pylops.Identity(10) * np.ones(10)'
python -c 'import pyproximal; print(pyproximal.__version__); pyproximal.L1(sigma=1.)'

echo 'Done!'

