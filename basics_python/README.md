# Python Basics

The questions in `submission.py` are simple problems to test your basic Python skills (and some basic math).
The entire problem should not take more than an hour of work.

## Questions

Below is an explanation of the questions. See the following section for the submission instructions.

### avrg_exclude_min_max
Compute the average of a set of numbers excluding a single instance of the minimum and maximum values.
For example, if the input is `[1,0,1,1,3,1]` then the average is `(1+1+1+1) / 4 = 1`, i.e. 0 and 3 are removed.
If the input is `[1,1,2,2]` then the average is `(1+2)/3 = 1`, i.e. a single instance of 1 and 2 are removed.
The problem should only take a few minutes and can be solved in a few lines of code.

### digits_prod_minus_sum
Compute the difference between the product and the sum of the digits of a natural number.
For example, if the input is `123`, then the digits are `1`, `2`, and `3`. Thus, the output is `1*2*3 - (1+2+3) = 6-6=0`.
The problem should only take a few minutes and can be solved in a few lines of code.


### check_pts_on_line
Check if a set of points belong to a straight line. This question is a little more involved than the above two questions as it relies on your basic math knowledge as well.
You can use the straight line equation to check if all points belong to one line.
For example, `[[1,1], [2,2], [3,3]]` belong to the same line, `y=x`.
However, `[[1,1], [2,2], [3,1]]` do not belong to the same line.
This problem should only take about 15 minutes.


## Submission
Update the `submission.py` script with your code and put the script in a folder titled `basics_python` before submitting it.