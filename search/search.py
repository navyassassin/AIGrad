# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's neighbors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's neighbors:", problem.getSuccessors(problem.getStartState()))
    


    stack = util.Stack()
    stack.push((problem.getStartState(), []))  # Store the current state and path

    visited = set()
    while not stack.isEmpty():
        current_state, path = stack.pop()
        if current_state not in visited:
            visited.add(current_state)
            if problem.isGoalState(current_state):

                return path  # Return the path when the goal state is reached
            children = problem.getSuccessors(current_state)
            for child, direction, cost in children:
                new_path = path + [direction]  # Extend the path
                stack.push((child, new_path))

    return []

    

    #util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    import util 

    queue = util.Queue()
    queue.push((problem.getStartState(), []))  # Store the current state and path
    visited = set()
    while not queue.isEmpty():
        current_state, path = queue.pop()
        if current_state not in visited:
            visited.add(current_state)
            if problem.isGoalState(current_state):
                return path  # Return the path when the goal state is reached
            children = problem.getSuccessors(current_state)
            for child, direction, cost in children:
                new_path = path + [direction]  # Extend the path
                queue.push((child, new_path))
    return []

    

"""
    fringe = util.Queue()                    # Fringe to manage which states to expand
    fringe.push(problem.getStartState())
    visited = []                        # List to check whether a state has already been visited
    path = []                           # List to store the final sequence of directions
    path_to_current = util.Queue()           # Queue to store directions to children (currState and path_to_current go hand in hand)
    curr_state = fringe.pop()
    while not problem.isGoalState(curr_state):
        if curr_state not in visited:
            visited.append(curr_state)
            successors = problem.getSuccessors(curr_state)
            for child, direction, cost in successors:
                fringe.push(child)
                temp_path = path + [direction]
                path_to_current.push(temp_path)
        curr_state = fringe.pop()
        path = path_to_current.pop()
    return path
"""

    #util.raiseNotDefined()


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    import util  

    queue = util.PriorityQueue()
    visited = set()
    final_line = []
    queue.push(problem.getStartState(), 0)
    while not queue.isEmpty():
        state = queue.pop()
        if state not in visited:
            visited.add(state)
            if problem.isGoalState(state):
                break
            children = problem.getSuccessors(state)
            for coord, child_direction, cost in children:
                temp_line = final_line + [child_direction]
                action_cost = problem.getCostOfActions(temp_line)
                if coord not in visited:
                    queue.push(coord, action_cost)
                    final_line.append(child_direction)
    return final_line

    #util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    
    queue = util.PriorityQueue()                    
    queue.push(problem.getStartState(),0)
    current_state = queue.pop()
    visited = []                                
    line=[]                                 
    path=[]                                    
    pathToCurrent=util.PriorityQueue()              
    while problem.isGoalState(current_state) != True:
        if current_state not in visited:
            visited.append(current_state)
            neighbors = problem.getSuccessors(current_state)
            for coord,direction,cost in neighbors:
                line = path + [direction]
                action_cost = problem.getCostOfActions(line) + heuristic(coord,problem)
                if coord not in visited:
                    queue.push(coord,action_cost)
                    pathToCurrent.push(line,action_cost)
        current_state = queue.pop()
        path = pathToCurrent.pop()    
    return path
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
