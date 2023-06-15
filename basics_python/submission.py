import numpy as np
import matplotlib.pyplot as plt
import math


class Solution:
    def avrg_exclude_min_max(self, vals: list[int]) -> float:
        """
        Compute the average of the list excluding the minimum and maximum elements
        e.g. vals = [1,0,1,1,3,1] --> avrg = 1+1+1+1 / 4 = 1  (0 and 3 removed)
        :param vals: list of integers
        :return: average value excluding max and min values
        """
        """
        Add your code here 
        """
        _min = None
        _max = None
        
        for ele in ls:
          if _min is None or _min > ele:
            _min = ele
          if _max is None or _max < ele:
            _max = ele
        
        if _min == _max or _min+1 == _max:
          return(0.0)
        
        
        _sum = 0
        _cnt = 0
        for ele in ls:
          if ele != _min and ele != _max:
            _sum = _sum + ele
            _cnt = _cnt + 1
        return(_sum/_cnt)

    def digits_prod_minus_sum(self, n: int) -> int:
        """
        Compute the difference between the product and the sum of the digits of n.
        e.g. n = 123 --> 1*2*3 - (1+2+3) = 6 - 6 = 0
        :param n: integer whose digits will be used to compute the difference
        :return: difference between the product and the sum of the digits
        """
        """
        Add your code here 
        """
        factorial = math.factorial(n)
        sum_of_natural_numbers = (n * (n + 1)) // 2
        
        return(factorial - sum_of_natural_numbers)

    def check_pts_on_line(self, coordinates: list[list[int]]) -> bool:
        """
        Check if the given points belong to a straight line.
        coordinates is a list of points. Each point is has [x,y] components
        e.g. coordinates = [[1,1], [2,2], [3,3]] --> points (1,1), (2,2), (3,3) are on the straight line y=x --> True
        e.g. coordinates = [[1,1], [2,2], [3,1]] --> points (1,1), (2,2), (3,1) do not belong to a straight line --> False
        :param coordinates: list of [x,y] pairs representing the points
        :return: True if the point belong to a straight line. False otherwise
        """
        """
        Add your code here
        """
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        #Calculating the slope
        m = (y2 - y1) / (x2 - x1)
        
        #Calculating the intercept by back substitution
        c = y2 - m*x2
        
        #If there are only two or less than two points they always form the line 
        if len(coordinates)<3:
          return True
        
        #Iterating over all the points and verifying
        for ele in coordinates:
          if ele[1] != m*ele[0]+c:
            return False

        return True
