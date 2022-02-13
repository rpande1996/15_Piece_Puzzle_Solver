import numpy as np

start = time.time()


# Creating a class to determine the node of the iteration. Node is the puzzle state.

class Node:

    # Defining the __init__ function

    def __init__(self, data, parent, act, cost):
        self.data = data
        self.parent = parent
        self.act = act
        self.id = self.get_id()
        self.cost = cost

    # Defining the __repr__ function

    def __repr__(self):

        data_shape = self.data.shape
        row_count = data_shape[0]
        col_count = data_shape[1]
        sep_str = ["|----" for _ in range(row_count)]
        sep_str.append("|\n")
        sep_str = "".join(sep_str)

        str_repr = sep_str

        # Creating a for loop to return the value in proper format

        for i in range(0, row_count):
            row_repr = ""
            for j in range(0, col_count):
                if self.data[i, j] > 9:
                    row_repr += f"| {self.data[i, j]} "
                else:
                    row_repr += f"|  {self.data[i, j]} "

            row_repr += "|\n"
            str_repr += row_repr
            str_repr += sep_str

        return str_repr

    # Defining a function to generate a unique id of the state of the puzzle.

    def get_id(self):
        _id = np.ravel(self.data).tolist()
        _id = [str(item) for item in _id]
        _id = "-".join(_id)
        self.id = _id
        return self.id


# Creating a class to convert a list into a queue

class Queue:

    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.append(node)

    def pop(self):
        node = self.queue[0]
        self.queue = self.queue[1:]
        return node

    def __len__(self):
        return len(self.queue)


# Move operations are done by checking the index value of the '0' element and checking the possible legal moves

# Defining a move function to move the blank value up
# When a 4x4 array is converted into a list, the index value of the topmost row becomes 0, 1, 2 and 3

def move_up(data):
    i = data.index(0)
    if (i == 0 or i == 1 or i == 2 or i == 3):
        return None
    else:
        data[i], data[i - 4] = data[i - 4], data[i]
    return data.copy()


# Defining a move function to move the blank value left
# When a 4x4 array is converted into a list, the index value of the leftmost row becomes 0, 4, 8 and 12

def move_left(data):
    i = data.index(0)
    if (i == 0 or i == 4 or i == 8 or i == 12):
        return None
    else:
        data[i], data[i - 1] = data[i - 1], data[i]
    return data.copy()


# Defining a move function to move the blank value down
# When a 4x4 array is converted into a list, the index value of the bottommost row becomes 12, 13, 14 and 15

def move_down(data):
    i = data.index(0)
    if (i == 12 or i == 13 or i == 14 or i == 15):
        return None
    else:
        data[i], data[i + 4] = data[i + 4], data[i]
    return data.copy()


# Defining a function to move the blank value right
# When a 4x4 array is converted into a list, the index value of the rightmost row becomes 3, 7, 11 and 15

def move_right(data):
    i = data.index(0)
    if (i == 3 or i == 7 or i == 11 or i == 15):
        return None
    else:
        data[i], data[i + 1] = data[i + 1], data[i]
    return data.copy()


# Defining a function to generate new legal moves as per the state

def generate_new_moves(state):
    list_states = []
    for func in [move_left, move_right, move_down, move_up]:
        dum_state = np.ravel(state.copy()).tolist()
        out_state = func(dum_state)
        if out_state is not None:
            list_states.append(np.reshape(out_state, (4, 4)))
    return list_states


def create_puzzle(inp):
    new_list = []
    init_list = []
    lis = inp.split()
    for i in lis:
        i = int(i)
        new_list.append(i)
    ideal_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    check_list = new_list.copy()
    check_list.sort()
    if check_list == ideal_list:
        init_list = new_list
    else:
        print("Re-enter correct values")
        exit(0)

    init_state = np.reshape(np.asarray(init_list), (4, 4))
    #
    return init_state


goal_state = np.asarray([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])

input_list = str(input("Enter input state: "))
init_state = create_puzzle(input_list)
state_queue = Queue()
state_queue.add(Node(init_state, None, None, None))

visited = []

# While loop to iterate the values inside the array with legal moves.
# If the current state is same as the goal state then the loop breaks.
# If the state ID is found in the visited list, then the node is skipped
while True:
    try:
        cur_node = state_queue.pop()
    except:
        if len([node for node in state_queue.queue]) == 0:
            break
    if np.all(cur_node.data == goal_state):
        break
    if cur_node.id in visited:
        continue
    moves = generate_new_moves(cur_node.data)
    for move in moves:
        new_node = Node(move, cur_node, None, None)
        state_queue.add(new_node)
    visited.append(cur_node.id)

target_node = cur_node
path = []

# While loop to add a step in the path

while cur_node is not None:
    path.append(cur_node)
    cur_node = cur_node.parent

# Traceback the path

path.reverse()

# Writing a text file to store the path

filename = "../output/nodePath_testcase.txt"
with open(filename, "w+") as sol_file:
    for node in path:
        str_node = np.ravel(node.data, order="F").tolist()
        str_node = [str(item) for item in str_node]
        str_node = " ".join(str_node) + "\n"
        sol_file.write(str_node)

print(path)
