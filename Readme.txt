15 Puzzle Problem using Breath First Search as following component

1. First we insert current node children into deque and then pop them one by one, following FIFO

2. For each child we check if that is goal state we return the path to that child 

3. Otherwise add the current node in visited list so that we do not traverse it again. Add this current node in graph by exploring all the directions Left, Right, Up, Down and then move on to next node in our frontier 


Instruction to run the progam - 

In Command Line right 

python breathfirst.py 

[ you will be prompted to enter the 15 puzzle numbers] enter them you will get your results. 

For example - 
python breathfirst.py 

initial configuration: 1 0 2 4 5 7 3 8 9 6 11 12 13 10 14 15

Result = 
{'Moves': ['R', 'D', 'L', 'D', 'D', 'R', 'R'], 'Number of Nodes expanded': 361, 'Time Taken': 0.005948066711425781, 'Memory Used': '392.0 KB'}


Please Note- Python version in use is 3.12.5



 ~ Saumya Chaudhary