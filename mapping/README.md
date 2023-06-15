# Mapping

This module provides basic questions to explain and test concepts related to mapping or building maps.
The module aims to test two areas:
- Theoretical concepts
- Programming skills.

## Questions

Below are the questions. See the following section for the submission instructions.

### Article: What are Occupancy Grid Maps
Read the following article (10 minute read):
- [https://automaticaddison.com/what-is-an-occupancy-grid-map/](https://automaticaddison.com/what-is-an-occupancy-grid-map/)
The article is also saved as a PDF.

In 1-2 sentences, answer each of the following questions:
- What is a grid map?  
  `From simulation point of view it is a 2x2 matrix which represents the factory floor.`
- What is an occupancy grid map?  
  `It is one step more in grid map where certain cells of the matrix are covered by some obstacles.`
- What coding/mathematical structure can you use to define an occupancy grid map?  
  `A 2x2 Matrix or also called as 2d array where obstacles denoted by some numeric value like 100 and free space by 0.`
- What could be a weakness of the occupancy grid map approach?  
  `Mapping grid into the real world. We need to assume some metric for resolution or mapping.`

### Programming question: random environment generator
Generate and plot a few random environments according the following requirements:
- The environment should be a 50×50 2D environment.
- Obstacles are labeled by 0 and free space labeled as 100.
- There should be a variable called `thresh` to determine whether a cell is an obstacle or free. This serves as a tuning knob.

Coding a basic solution may take about 10 minutes and can be done in just a few lines of code. You may need more time if you are not familiar with Python operators and functions.

Hints:
- Use numpy arrays for the map and matplotlib pyplot to plot.
- Generating a random map can be done in 1 line of code. Don't overstress it if you need more lines of code.
- Try to use the `rand` function to generate random numbers (check out its documentation). 


### Follow-up questions
Once you have your random environment generator working, answer the following questions. Your answer should only be a few sentences.
- What happens when you increase/decrease thresh? Please provide images of the environment with the higher/lower thresh values.
- What does it mean if a cell had a value between 0 and 100? Where could/Why would this be useful?
- (Optional) Bonus Question: Can you generate the random map in 1 line of code? (i.e. other than thresh definition and the plotting code, you only have 1 line of code)

## Submission
Create a folder called `mapping` and include the following files:
- Create a document (word, txt, ...) titled `article` with your answers to the article questions.
- Update the `submission.py` script with your code and add it to the folder.
- Create a document (word, txt, ...) titled `followup` with your answers to the follow-up questions. Include some figures.
