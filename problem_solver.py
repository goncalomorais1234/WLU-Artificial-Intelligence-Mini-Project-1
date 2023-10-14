import math
import random

def simulated_annealing(G, E, W, Dv, A, initial_temp, cooling_rate):
    current_state = W
    current_cost = path_cost(current_state, G)
    best_state = current_state
    best_cost = current_cost
    temperature = initial_temp

    while temperature > 1:
        available_actions = actions(current_state, G, A, E)
        action = random.choice(available_actions)

        new_state = result(current_state, action)
        new_cost = path_cost(new_state, G)
        cost_diff = new_cost - current_cost

        if cost_diff < 0 or random.uniform(0, 1) < math.exp(-cost_diff / temperature):
            current_state = new_state
            current_cost = new_cost

            if current_cost < best_cost:
                best_state = current_state
                best_cost = current_cost

        temperature *= cooling_rate

    return best_state
