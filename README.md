# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*
We know that each cell in 3*3 box, or in a column or a row has to have a unique number from 0 to 9.
However, when solving the problems we may find cells can have multiple choices.  Now, if 2 cells ( in the same box, column, or row) share all but one digit, one can assume that the digits they don't share is the number that each cell can have).  Hence, knowing the constraints and that each cell can have only one and only one distinct number helps us reduce use of search algorithm.
Here is my Algorithm
Sorry, I totally forget to add it here.  I had it in the code.
#Get a value in the grid.  Make sure that the value as at least 2 digits.
#Find its its units
#In each unit, check if a duplicate exists, if it does go over the unit and replace its digits
# from all the other boxes.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
  Find the unit or units of 2 coordinates with the same 2 digits values, then just see their digits are shared by other cells.  If yes, remove the digits from the other cells. 
A: *Student should provide answer here*
There is no need for a new code to deal with this case, I just added the coordinates in the diagonal to unitlist, and made sure 
 coordinates on diagonal have their peers list, and units updates to have their giving diagonal.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
