# CONLab Behavioral Design and Motion Planning Project Onboarding
This package includes some basics to get started with motion planning for autonomous vehicles.
Please install any dependencies (see below) then solve the modules. Each module includes its own README instructions.
Once done, compress the folder with all the solutions and send it to Sleiman.Safaoui@utdallas.edu.
Good luck!

## Installation
Install the package by following these steps.

1. Install the dependencies
   - (Linux) Using the setup shell script
   ```commandline
    ./setup.sh
    ```
   - Using conda (if you have [conda installed](https://docs.anaconda.com/anaconda/install/))
   ```commandline
    conda env create -f requirements/environment.yml
    ```
   - Using pip
   ```commandline
    pip install -r requirements/requirements.txt
    ```
   - You can also set up the Python interpreter and install the packages described in `requirements/requirements.txt` manually (e.g. using [PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux)'s add interpreter/interpreter settings)
2. Code and Run the scripts!

## Order
The following order is recommended:

1. basics_python
2. mapping
3. motion_planning
4. control