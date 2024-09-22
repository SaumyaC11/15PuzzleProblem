import time
import math
import psutil
import os
from collections import deque


class Board:
    def __init__(self, tiles):
        self.size = int(math.sqrt(len(tiles)))
        self.tiles = tiles

    def execute_action(self, action):
        new_tiles = self.tiles[:]
        zero_index = new_tiles.index('0')

        if action == 'L':
            if zero_index % self.size > 0:
                new_tiles[zero_index - 1], new_tiles[zero_index] = new_tiles[zero_index], new_tiles[zero_index - 1]
        if action == 'R':
            if zero_index % self.size < (self.size - 1):
                new_tiles[zero_index + 1], new_tiles[zero_index] = new_tiles[zero_index], new_tiles[zero_index + 1]
        if action == 'U':
            if zero_index - self.size >= 0:
                new_tiles[zero_index - self.size], new_tiles[zero_index] = new_tiles[zero_index], new_tiles[
                    zero_index - self.size]
        if action == 'D':
            if zero_index + self.size < self.size * self.size:
                new_tiles[zero_index + self.size], new_tiles[zero_index] = new_tiles[zero_index], new_tiles[
                    zero_index + self.size]
        return Board(new_tiles)


class Node:
    def __init__(self, state, parent, action):
        # characteristics associated with a node
        self.state = state
        self.parent = parent
        self.action = action


def goal_state(curr_tiles):
    # to check if we have reached our goal state
    return curr_tiles == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']


def find_path_to_parent(node):
    # finding the path back to root node - ( gives final action string)
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    path = path[::-1]
    return path


def expand(node):
    # we will expand the current node into four possible direction and add then to the graph
    child = []
    action = ['L', 'R', 'U', 'D']
    for i in action:
        child_state = node.state.execute_action(i)
        new_node = Node(child_state, node, i)
        child.append(new_node)
    return child


def breath_first_search(root_node):
    # the main function of breath first search according to pseudocode of AIMA
    start_time = time.time()
    # frontier is a deque ( double ended queue and we will perform pop from left thus implementing FIFO
    frontier = deque([root_node])
    # hash set storing all the visited node also known as reached in AIMA
    close_set = set()
    count = 0
    while len(frontier) > 0:
        current_node = frontier.popleft()
        # increase the count of number of state visited
        count += 1
        # add the current node into visited set
        close_set.add(tuple(current_node.state.tiles))
        

       
        for child in expand(current_node):
            # check if we are already at goal state if yet call function that return path to the current node and end the function
            if goal_state(child.state.tiles):
                path = find_path_to_parent(child)
                end_time = time.time()
                return path, count, (end_time - start_time)
            elif tuple(child.state.tiles) in close_set:
                continue
            else:
                # else for each node expand the graph to it's child
                frontier.append(child)

    print("Frontier is empty")
    return False


def main():
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024.0
    initial = str(input("initial configuration: "))
    initial_list = initial.split(" ")
    root = Node(Board(initial_list), None, None)
    # formatting the result to a dictionary
    result = breath_first_search(root)
    final_memory = process.memory_info().rss / 1024.0
    params = ["Moves", "Number of Nodes expanded", "Time Taken", "Memory Used"]
    formatted_result = {}
    for param, value in zip(params, result):
        formatted_result[param] = value
    formatted_result[params[-1]] = str(final_memory - initial_memory) + " KB"
    print(formatted_result)


if __name__ == "__main__":
    main()
