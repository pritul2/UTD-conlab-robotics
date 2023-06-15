# Control

This module provides basic questions to explain and test concepts related to control, interpreting graphs, and using python.
The module aims to test three areas:
- Theoretical concepts
- Graph analysis skills
- Using Python classes and functions.

## Questions

Below are the questions. See the following section for the submission instructions.

### Article: PID Controllers
Read the "Fundamental Operation" part of the Wikipedia article on PID control (15 minute read):
- [https://en.wikipedia.org/wiki/PID_controller](https://en.wikipedia.org/wiki/PID_controller)

In 1-2 sentences, answer each of the following questions:
- What is the error signal (i.e. the error as a function of time)?   
`It is the difference between the measured set point and the process variable. So we need to tune our controller such that the error goes near to zero.`
- What are the three terms of PID control?   
`P: Proportional, I: Integral: D: Derivative. Proportional will provides the magnitude of the error. Integral sum up all the error and helps in accumulating the past errors. Derivative acts as a resistance and minimize the error residual.`
- What is the control input equation for a P controller (pure proportional controller) in terms of the error signal e(t)?    
`Proportional Gain = Po + Kp * ( change in error )`  

### Programming question: P-controlled robot
We will control a robot using a P controller. The robot has two states, one for each spatial dimension (i.e. the two states represent the robot's position in a flat plane). 
The two states are concatenated into a single 2x1 vector called `x`.
The robot dynamics are the simplified single integrator dynamics; i.e. the robot's next position is simply the current position plus the control input (plus a noise term)
The robot dynamics are described by the class `SingleIntegrator2d` in `dynamics.py`.
The class has two methods: `step` which moves the robot forward and `predict` which predicts where the robot will be.

Fill-in the 5 missing lines of code in the `submission.py` script. 
If you are not familiar with Python classes, methods, and functions, please check out the following resources.
- Functions: [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp)
- Classes and methods: [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp)

Coding this is relatively easy and can be done in a few minutes. However, getting familiar with the Python syntax and reading through the code may take a while and depends on your experience.

Hints:
- Read the comments carefully
- Do not overthink things


### Follow-up questions
With the code running, we will now analyze the system. This might take around 40 minutes.
You may have noticed the noise term `w_t` appearing in the code and the two variables `w_mean_t` and `w_std_dev_t`.
Noise is a randomly generated value that always exists in real life. 
In this setting, we simply add the noise to the dynamics so that the true robot position is what we expect plus a random noise value.
Thus, the true position we realize is generally never exactly as the prediction.
This noise value can be generated based on various probability distributions. For simplicity, we consider the Gaussian (i.e. Normal) distribution in this case.
This distribution is characterized by two values: the mean (`w_mean_t`) and standard deviation (`w_std_dev_t`).
For more information about this noise, check out the following two resources:
- Wikipedia article [https://en.wikipedia.org/wiki/Normal_distribution](https://en.wikipedia.org/wiki/Normal_distribution)
- Python function: [https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy-random-normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html#numpy-random-normal)

The default noise is set to zero. That is indicated by the `0.00` coefficient of `w_std_dev_t`.
We start by analyzing the system with no noise; specifically, we analyze the two figures that are plotted.
- What does the "Robot Trajectory" figure represent?
- Does the presented trajectory make sense?
- What do the two plots of the second figure ("Dimension 1 trajectory" and "Dimension 2 trajectory") represent?
- Is the controller working?
- Try changing the gain `kp` from `[0.1, 0.1]` to `[0.5, 0.5]` then to `[0.05, 0.05]`. How does `kp` affect the robot?
Setting `kp` back to `[0.1, 0.1]` we will now add noise. 
Note that when running with noise, you may have to run the code a few times to see how the results may change with every run due to noise.
(You may want to print out the noise value. That's optional but might help with your analysis)
- Before changing the noise, what do you expect will happen when noise is added?
- Increase the `w_std_dev_t` coefficient from `0.00` to `0.03`. What happens to the robot?
- If we increase the noise value further, what do you expect will happen?
- Increase the `w_std_dev_t` coefficient to `0.1`. What happens to the robot?
- If we increase the noise a lot, what do you expect will happen? Will the robot be able to reach the goal?
- Increase the `w_std_dev_t` coefficient to `1`. What happens to the robot?

## Submission
Create a folder called `control` and include the following files:
- Create a document (word, txt, ...) titled `article` with your answers to the article questions.
- Update the `submission.py` script with your code and add it to the folder.
- Create a document (word, txt, ...) titled `followup` with your answers to the follow-up questions. Include some figures.
