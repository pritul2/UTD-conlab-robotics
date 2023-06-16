# Motion Planning

This module provides basic questions to explain and test concepts related to motion planning.

## Questions

Below are the questions. See the following section for the submission instructions.

### A* Algorithm
A* is a popular path planning algorithm. You can find a GIF of it in action [here](https://github.com/AtsushiSakai/PythonRobotics#a-algorithm) and Python code for it [here](
    
).

1. Use any resources to learn about A*. Then, summarize, in your own words, what it is and how it works in 2-3 sentences. You may comment on things like its optimality, completeness, efficiency, pros and cons, or performance relative to other algorithms.
`A* is a optimal path finding algorithm calculated on shortest distance + heuristic or estimated value. It is better path searching algorithm than dijkstra where it is searching fewer possible nodes because of heuristic value. Optimality: It is optimal and can find shortest path with less convergence. Completeness: It will never overestimate and considered complete algorithm. It is effecient because it explores less nodes. Pros: Effective and completeness. Cons: Relies on heuristic value and requires more memory in computation. Dijkstra's algorithm is a reliable and simple approach for finding shortest paths, A* incorporates a heuristic to improve efficiency, and D* is designed for dynamic environments. `
2. Run the A* algorithm with different goal locations and grid sizes. Generate some figures (3-6 figures) and describe any differences you observe (just a few of sentences). You do NOT have to write the algorithm's code yourself. You can use any implementation. If the code is available online, simply include a link to it in your submission. Otherwise, please include the code in your submission.   
`The algorithm able to finds the destination path irrespective of wherever the goal location is. When there is lesser grid size the algorithm converges slower and explore more possibilities but it reaches the destination. Whereas, when the grid size is larger the algorithm converges fast and may also overshoot the obstacle when reaching to the destination. As what seen when grid size is greater than 3.0`

## Submission
Create a folder called `motion_planning` and include the following files:
- Create a word document titled `solution` with your answers to questions 1 and 2 (including the figures).
- If you wrote code, include it as well.
