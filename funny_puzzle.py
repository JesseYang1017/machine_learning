import heapq
import copy


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    distance = 0
    state_org = [from_state[0:3], from_state[3:6], from_state[6:9]]
    state_correct = [to_state[0:3], to_state[3:6], to_state[6:9]]
    for i in range(3):
            for j in range(3):
                Used = False
                for i1 in range(3):
                    for j1 in range(3):
                        if state_org[i][j] == state_correct[i1][j1] and state_org[i][j] != state_correct[i][j] and Used == False and state_org[i][j] != 0:
                            distance += abs(i - i1) + abs(j - j1)
                            Used = True
    return distance




def print_succ(state):
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):
    state_temp = [state[0:3], state[3:6], state[6:9]]
    succ_states = []
    for row in range(len(state_temp)):
        for col in range(len(state_temp)):
            if state_temp[row][col] == 0:
                succ_states.append(up(state_temp, row, col)) # (row-1)(col)
                succ_states.append(down(state_temp, row, col)) # (row+1)(col)
                succ_states.append(left(state_temp, row, col)) # (row)(col-1)
                succ_states.append(right(state_temp, row, col)) #
                # succ_states.append(upleft(state_temp, row, col))
                # succ_states.append(upright(state_temp, row, col))
                # succ_states.append(downleft(state_temp, row, col))
                # succ_states.append(downright(state_temp, row, col))
    succ_states = list(filter(None, succ_states))
    return sorted(succ_states)

def up(k, i, j):
    state = copy.deepcopy(k)
    if i - 1 >= 0 and state[i - 1][j] != 0:
        state[i][j], state[i - 1][j] = state[i - 1][j], state[i][j]
        state = [j for sub in state for j in sub]
        return state

def down(k, i, j):
    state = copy.deepcopy(k)
    if i + 1 < len(state) and state[i + 1][j] != 0:
        state[i][j], state[i + 1][j] = state[i + 1][j], state[i][j]
        state = [j for sub in state for j in sub]
        return state

def left(k, i, j):
    state = copy.deepcopy(k)
    if j - 1 >= 0 and state[i][j - 1] != 0:
        state[i][j], state[i][j - 1] = state[i][j - 1], state[i][j]
        state = [j for sub in state for j in sub]
        return state

def right(k, i, j):
    state = copy.deepcopy(k)
    if j + 1 < len(state) and state[i][j + 1] != 0:
        state[i][j], state[i][j + 1] = state[i][j + 1], state[i][j]
        state = [j for sub in state for j in sub]
        return state

def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    """
    TODO: Implement the A* algorithm here.

    INPUT: 
        An initial state (list of length 9)

    WHAT IT SHOULD DO:
        Prints a path of configurations from initial state to goal state along  h values, number of moves, and max queue number in the format specified in the pdf.
    """
    
    pq = []
    h = get_manhattan_distance(state)
    heapq.heappush(pq,(h, state, (0, h, -1)))
    close = []
    index = 0
    while True:
        if len(pq) == 0:
            break
        n = heapq.heappop(pq)
        # If OPEN is empty, exit with failure
        # Remove from OPEN and place on CLOSED a node n for which f(n) is minimum
        # for i in open:
        #     if i[2][0] + i[2][1] < n[2][0] + n[2][1]: 
        #         n = i
        #         open.remove(n)
        #         heapq.heappush(close, n)
        # If n is a goal node, exit
        if n[1] == goal_state:
            steps = list()
            current = n
            #Keep tracing back until reaching the initial state
            while True:
                steps.insert(0,current[1])
                if current[2][2] == -1:
                    break
                else:
                    current = close[current[2][2]]
            #Print out all the steps taken
            for i in range(len(steps)):
                print(str(steps[i]) + ' h='+ str(get_manhattan_distance(steps[i])) + ' moves: '+ str(i))
            print("Max queue length: " + str(len(pq) + 1))
            return
        else:
            close.append(n)
            g = n[2][0]+1
            n_all = get_succ(n[1])
            for n_1 in n_all:
                check  = -1
                for i in range(len(close)):
                    if close[i][1] == n_1:
                        check = i
                        break 
                if check == -1 :
                    h = get_manhattan_distance(n_1)
                    heapq.heappush(pq,( g + h , n_1, (g , h, index)))
                else:
                    if close[check][2][0] > g :
                        close[check] = ( g + h , n_1, (g , h, index))
            index += 1

if __name__ == "__main__":
    """
    Feel free to write your own test code here to exaime the correctness of your functions. 
    Note that this part will not be graded.
    """
    # print_succ([2,5,1,4,0,6,7,0,3])
    # print()

    print(get_manhattan_distance([2,5,1,4,3,6,7,0,0], [1, 2, 3, 4, 5, 6, 7, 0, 0]))
    print()

    solve([2,5,1,4,3,6,7,0,0])
    print()
