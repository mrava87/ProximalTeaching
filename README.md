# An introduction to proximal solvers for engineers

Material for course on **An introduction to proximal solvers for engineers**, to be taught internally at 
at [Luna Innovations](http://lunainc.com).

## Teaching Material

### Lectures
The main teaching material is available in the ``lectures`` directory the form of Jupyter slides, divided into 3 separate lectures. 

Simply type ``jupyter nbconvert Lecture*.ipynb --output-dir='../html' --to slides --post serve --embed-images`` (where ``*=1,2,3``) to obtain the slides in html format. Note that the html version of the slides is also already provided in the ``html`` subdirectory.

### Exercises
Alongside the lecture slides, a number of exercises will be presented during the course. These are in the form of Jupyter notebooks and can be accessed from the ``notebooks`` directory.

## Teaching Schedule

| Session                         |            Link to material         |            Link to Colab         |
|---------------------------------|-------------------------------------|----------------------------------|
| Lecture 1                       | [Link](lectures/Lecture1.ipynb)     |
| Lecture 2                       | [Link](notebooks/Lecture2.ipynb)    |
| Lab1: FFTLinOp.ipynb            | [Link](examples/FFTLinOp.ipynb)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrava87/ProximalTeaching/blob/main/examples/FFTLinOp.ipynb)  |
| Lab2: BasisPursuit.ipynb            | [Link](examples/FFTLinOp.ipynb)     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PyLops/mrava87/ProximalTeaching/blob/main/examples/BasisPursuit.ipynb)  |


## Getting started

To run the different Jupyter notebooks, participants can either use:

- local Python installation (simply run ``./install_env.sh``).
- a Cloud-hosted environment such as Google Colab. Simply make sure to upload the relevant notebooks and run the first comment cell to install missing libraries.
